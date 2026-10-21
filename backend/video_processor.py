"""Módulo de processamento de vídeo para detecção e heatmap (Synapse 3D)"""

import cv2
import numpy as np
from ultralytics import YOLO
from typing import List, Dict, Optional
import json
import os


class VideoProcessor:
    def __init__(self, model_path: str = "yolov8n.pt", confidence: float = 0.5):
        self.model = YOLO(model_path)
        self.confidence = confidence
        self.heatmap_accumulator: Dict[str, np.ndarray] = {}

    def process_frame(self, camera_id: str, frame: np.ndarray) -> Dict:
        """
        Processa um único frame da câmera.
        Retorna detecções e atualiza o acumulador de heatmap.
        """
        results = self.model(frame, conf=self.confidence, verbose=False)
        detections = []

        h, w = frame.shape[:2]

        # Inicializar acumulador de heatmap para esta câmera
        if camera_id not in self.heatmap_accumulator:
            self.heatmap_accumulator[camera_id] = np.zeros((h, w), dtype=np.float32)

        for r in results:
            boxes = r.boxes
            if boxes is None:
                continue
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                conf = box.conf[0].cpu().numpy()
                cls = int(box.cls[0].cpu().numpy())

                # Classe 0 = pessoa no COCO
                if cls == 0:
                    cx = int((x1 + x2) / 2)
                    cy = int((y1 + y2) / 2)

                    # Acumular heatmap (área onde a pessoa esteve)
                    self.heatmap_accumulator[camera_id][
                        max(0, cy - 10) : min(h, cy + 10),
                        max(0, cx - 10) : min(w, cx + 10),
                    ] += 1.0

                    detections.append(
                        {
                            "bbox": [float(x1), float(y1), float(x2), float(y2)],
                            "center": [float(cx), float(cy)],
                            "confidence": float(conf),
                            "class": "person",
                        }
                    )

        return {
            "camera_id": camera_id,
            "detections": detections,
            "frame_shape": [h, w],
        }

    def get_heatmap_data(self, camera_id: str) -> Optional[List[Dict]]:
        """
        Retorna os pontos de heatmap para uma câmera.
        """
        if camera_id not in self.heatmap_accumulator:
            return None

        acc = self.heatmap_accumulator[camera_id]
        if acc.max() == 0:
            return []

        # Normalizar para 0-1
        acc_norm = acc / acc.max()

        h, w = acc_norm.shape
        points = []
        step = 10  # redução de resolução para performance

        for y in range(0, h, step):
            for x in range(0, w, step):
                intensity = float(acc_norm[y, x])
                if intensity > 0.1:
                    points.append(
                        {
                            "x": x / w,  # normalizado 0-1
                            "y": y / h,  # normalizado 0-1
                            "intensity": intensity,
                        }
                    )

        return points

    def reset_heatmap(self, camera_id: str):
        if camera_id in self.heatmap_accumulator:
            self.heatmap_accumulator[camera_id].fill(0)

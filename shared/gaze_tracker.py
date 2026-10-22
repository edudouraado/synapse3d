"""Módulo de estimativa de direção do olhar (aproximada via detecção de face)"""

import cv2
import numpy as np
from typing import Tuple, Dict


class GazeTracker:
    def __init__(self):
        # Carregar classificadores Haar do OpenCV (já vem instalado com opencv-python)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

    def estimate_gaze(self, frame: np.ndarray, bbox: Tuple[int, int, int, int]) -> Dict:
        """
        Estima a direção do olhar com base na detecção de face dentro do bounding box da pessoa.
        Retorna dicionário com direção e confiança aproximada.
        """
        x1, y1, x2, y2 = bbox

        # Recortar região da pessoa para buscar face
        person_roi = frame[y1:y2, x1:x2]

        if person_roi.size == 0:
            return {"direction": "unknown", "confidence": 0.0, "face_detected": False}

        gray = cv2.cvtColor(person_roi, cv2.COLOR_BGR2GRAY)

        # 1. Tentar face frontal (olhando para a câmera)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        if len(faces) > 0:
            return {
                "direction": "front",
                "confidence": 0.8,
                "face_detected": True
            }

        # 2. Tentar perfil (virado para os lados)
        profiles = self.profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        if len(profiles) > 0:
            px, py, pw, ph = profiles[0]
            person_w = x2 - x1
            # Posição relativa do rosto dentro do corpo da pessoa
            center_offset = (px + pw / 2) / person_w if person_w > 0 else 0.5

            if center_offset < 0.45:
                return {"direction": "left", "confidence": 0.6, "face_detected": True}
            elif center_offset > 0.55:
                return {"direction": "right", "confidence": 0.6, "face_detected": True}
            else:
                return {"direction": "front", "confidence": 0.5, "face_detected": True}

        # 3. Sem face detectada
        return {"direction": "unknown", "confidence": 0.0, "face_detected": False}

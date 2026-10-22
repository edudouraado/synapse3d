"""Script de teste da camera RTSP com deteccao de pessoas e direcao do olhar (Synapse 3D)"""

import cv2
from backend.video_processor import VideoProcessor
from shared.gaze_tracker import GazeTracker

# URL RTSP da CAM 4 (senha codificada: % -> %25)
rtsp_url = "rtsp://suporteti:root%259893@192.168.10.111:554/cam/realmonitor?channel=4&subtype=0"

cap = cv2.VideoCapture(rtsp_url)
processor = VideoProcessor()
gaze_tracker = GazeTracker()

if not cap.isOpened():
    print("Nao foi possivel abrir a camera.")
    print("   Verifique se a URL RTSP esta correta e se o gravador esta ligado.")
    exit()

print("Camera conectada!")
print("   Pressione 'q' para sair.")
print("   Arraste a borda da janela para redimensionar.")

cv2.namedWindow("Synapse 3D - Teste Camera CAM 4", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Synapse 3D - Teste Camera CAM 4", 1280, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resultado = processor.process_frame("cam_001", frame)

    for det in resultado["detections"]:
        x1, y1, x2, y2 = [int(v) for v in det["bbox"]]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Estimar direcao do olhar
        gaze = gaze_tracker.estimate_gaze(frame, (x1, y1, x2, y2))

        # Texto da pessoa
        label = f"Pessoa {det['confidence']:.2f}"
        gaze_label = f"Olhar: {gaze['direction']}"

        if gaze['face_detected']:
            label_color = (0, 255, 0)   # verde se detectou face
        else:
            label_color = (0, 165, 255) # laranja se nao detectou face

        cv2.putText(frame, label, (x1, y1 - 10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, label_color, 1)
        cv2.putText(frame, gaze_label, (x1, y2 + 20),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, label_color, 1)

    cv2.imshow("Synapse 3D - Teste Camera CAM 4", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Teste finalizado.")
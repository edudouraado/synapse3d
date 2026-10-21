"""Script de teste da camera RTSP com deteccao de pessoas (Synapse 3D)"""

import cv2
from backend.video_processor import VideoProcessor

# URL RTSP da CAM 4 (senha codificada: % -> %25)
rtsp_url = "rtsp://suporteti:root%259893@192.168.10.111:554/cam/realmonitor?channel=4&subtype=0"

cap = cv2.VideoCapture(rtsp_url)
processor = VideoProcessor()

if not cap.isOpened():
    print("Nao foi possivel abrir a camera.")
    print("   Verifique se a URL RTSP esta correta e se o gravador esta ligado.")
    exit()

print("Camera conectada!")
print("   Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resultado = processor.process_frame("cam_001", frame)

    for det in resultado["detections"]:
        x1, y1, x2, y2 = [int(v) for v in det["bbox"]]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"Pessoa {det['confidence']:.2f}", (x1, y1-10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow("Synapse 3D - Teste Camera CAM 4", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Teste finalizado.")

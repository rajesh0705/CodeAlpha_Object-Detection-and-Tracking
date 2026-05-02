from ultralytics import YOLO

class YOLODetector:
    def __init__(self):
        self.model = YOLO("models/yolov8n.pt")

    def detect(self, frame):
        results = self.model(frame)[0]
        detections = []

        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])

            label = self.model.names[cls]  # ✅ object name

            # Store: box + confidence + label
            detections.append([x1, y1, x2, y2, conf, label])

        return detections
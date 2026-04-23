from ultralytics import YOLO

class YOLODetector:
    def __init__(self):
        self.model = YOLO("weights/yolov8n.pt")

    def detect(self, frame):
        results = self.model(frame)[0]

        detections = []

        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])

            w = x2 - x1
            h = y2 - y1

            # ✅ Correct format for Deep SORT
            detections.append(([x1, y1, w, h], conf, cls))

        return detections
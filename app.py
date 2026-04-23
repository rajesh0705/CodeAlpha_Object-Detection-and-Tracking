import cv2
from models.yolo_model import YOLODetector
from models.tracker import Tracker
from utils.draw_utils import draw_boxes

def main():
    cap = cv2.VideoCapture(0)  # or your video path

    detector = YOLODetector()
    tracker = Tracker()

    # ✅ Make window resizable
    cv2.namedWindow("Detection & Tracking", cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # ✅ Resize frame to full screen size
        frame = cv2.resize(frame, (1280, 720))   # you can try (1920,1080)

        # Detection
        detections = detector.detect(frame)

        # Tracking
        tracks = tracker.update(detections, frame)

        # Draw boxes
        frame = draw_boxes(frame, tracks)

        # Show output
        cv2.imshow("Detection & Tracking", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
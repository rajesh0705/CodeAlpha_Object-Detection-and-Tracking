import cv2

def draw_boxes(frame, tracks):
    for track in tracks:
        x1, y1, x2, y2 = track["bbox"]
        track_id = track["id"]
        label = track["label"]
        conf = track["conf"]

        # Green bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Text (object name + confidence)
        text = f"{label} {conf:.2f}"

        # Background for text (better visibility)
        (w, h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        cv2.rectangle(frame, (x1, y1 - 25), (x1 + w, y1), (0, 255, 0), -1)

        # Put text above box
        cv2.putText(frame, text, (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 0), 2)

    return frame
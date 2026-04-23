import cv2

def draw_boxes(frame, tracks):
    for obj in tracks:
        x, y, w, h = obj["bbox"]
        track_id = obj["id"]

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw ID
        cv2.putText(frame, f"ID: {track_id}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return frame
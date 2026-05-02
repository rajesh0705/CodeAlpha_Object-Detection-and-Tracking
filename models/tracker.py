class Tracker:
    def __init__(self):
        pass

    def update(self, detections, frame):
        tracks = []

        for det in detections:
            x1, y1, x2, y2, conf, label = det

            track_id = 0  # or your SORT ID

            tracks.append({
                "bbox": [x1, y1, x2, y2],
                "id": track_id,
                "label": label,   # ✅ keep label
                "conf": conf
            })

        return tracks
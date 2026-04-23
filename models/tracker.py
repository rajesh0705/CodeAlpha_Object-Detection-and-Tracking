from deep_sort_realtime.deepsort_tracker import DeepSort

class Tracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30)

    def update(self, detections, frame):
        tracks = self.tracker.update_tracks(detections, frame=frame)

        tracked_objects = []

        for track in tracks:
            if not track.is_confirmed():
                continue

            track_id = track.track_id
            l, t, w, h = map(int, track.to_ltrb())

            tracked_objects.append({
                "id": track_id,
                "bbox": (l, t, w, h)
            })

        return tracked_objects
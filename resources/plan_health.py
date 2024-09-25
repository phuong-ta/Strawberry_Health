import cv2
import numpy as np
from ultralytics import YOLO

class Plan_Health:
    def __init__(self, yolo_model_path, camera_id, zoom_factor):
        # Initialize the YOLO model
        self.model = YOLO(yolo_model_path)
        # Initialize the video capture object with the given camera ID
        self.cap = cv2.VideoCapture(camera_id)
        # Set the zoom factor
        self.zoom_factor = zoom_factor

        if not self.cap.isOpened():
            raise Exception("Error: Could not open video stream.")

    def zoom_in(self, frame):
        h, w = frame.shape[:2]
        center_x, center_y = w // 2, h // 2

        # Calculate the region of interest (ROI) coordinates
        radius_x, radius_y = int(w / (2 * self.zoom_factor)), int(h / (2 * self.zoom_factor))

        min_x, max_x = center_x - radius_x, center_x + radius_x
        min_y, max_y = center_y - radius_y, center_y + radius_y

        # Crop and resize the ROI to the original frame size
        cropped = frame[min_y:max_y, min_x:max_x]
        zoomed_frame = cv2.resize(cropped, (w, h))

        return zoomed_frame

    def start_detection(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Zoom in
            zoomed_frame = self.zoom_in(frame)

            # Use YOLO to detect objects
            results = self.model(zoomed_frame)

            # Draw the bounding boxes on the zoomed frame
            annotated_frame = results[0].plot()

            # Display the result
            cv2.imshow('YOLOv8 Detection', annotated_frame)

            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the capture and close windows
        self.cap.release()
        cv2.destroyAllWindows()

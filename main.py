from ultralytics import YOLO
from resources.object_detection_in_image import detect_objects_in_image
import cv2


def track_objects(model, cam_number):
    cap = cv2.VideoCapture(cam_number)

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 tracking on the frame, persisting tracks between frames
            results = model.track(frame, persist=True, save=False)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("YOLOv8 Tracking", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()


# Model
model_path = YOLO("C:/Users/phuongta/Desktop/ML/Strawberry_Health/runs/detect/train4/weights/last.pt")
# Stream
video_file2 = 0
# Image
image_file_path = "C:/Users/phuongta/Desktop/ML/Strawberry_Health/sources/unhealthy/purple_light/leaf4.jpg"

# track_objects(model_path, video_file2)

# detect object in image
detections = detect_objects_in_image(model_path, image_file_path)
# Process the detections
for class_name, box in detections:
    print(f"Object: {class_name}, Bounding Box: {box}")

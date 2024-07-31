import cv2
from ultralytics import YOLO
from resources.mqtt.mqtt_publisher import publish_msg


def track_objects(model_path, cam_number):
    # open camera
    cap = cv2.VideoCapture(cam_number)

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:

            # Run YOLOv8 tracking on the frame, persisting tracks between frames
            results = model_path.track(frame, device=0, persist=True, save=False)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("Cam" + str(cam_number), annotated_frame)

            # get class name of detected object
            first_detection = results[0]
            # boxes = first_detection.boxes.xyxy.cpu().numpy()
            class_indices = first_detection.boxes.cls.cpu().numpy().astype(int)
            trained_model_path = YOLO("C:/Users/phuongta/Desktop/ML/Strawberry_Health/runs/detect/train4/weights/last.pt")
            class_names = [trained_model_path.model.names[i] for i in class_indices]
            #print(class_names)
            """
            if len(class_names) > 0:
                publish_msg(cam_id=cam_number, msg="".join(class_names))
                """
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()

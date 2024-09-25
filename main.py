from ultralytics import YOLO
from resources.object_detection_in_image import detect_objects_in_image
from resources.object_detection_with_camera import track_objects
from resources.plan_health import Plan_Health
from threading import Thread


if __name__ == '__main__':
    #model_path = YOLO("runs/detect/train4/weights/last.pt")
    model_path = "runs/detect/train4/weights/last.pt"
    camera_id = 0
    zoom_factor = 2
    strarberry_health = Plan_Health(yolo_model_path = model_path, camera_id = camera_id, zoom_factor = zoom_factor)
    strarberry_health.start_detection()


    # Image
    #image_file_path = "C:/Users/phuongta/Desktop/ML/Strawberry_Health/sources/unhealthy/purple_light/leaf4.jpg"

    # track object with camera.
    # track_objects(model, cam_id)
    """
    tracker_thread1 = Thread(target=track_objects, args=(model_path, cam1_id), daemon=True)
    tracker_thread2 = Thread(target=track_objects, args=(model_path, cam2_id), daemon=True)

    tracker_thread1.start()
    tracker_thread2.start()
    tracker_thread1.join()
    tracker_thread2.join()
    """

    """
    # detect object in image
    detections = detect_objects_in_image(model_path, image_file_path)
    # Process the detections
    for class_name, box in detections:
        print(f"Object: {class_name}, Bounding Box: {box}")
    """

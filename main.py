from ultralytics import YOLO
from resources.object_detection_in_image import detect_objects_in_image
from resources.object_detection_with_camera import track_objects
from threading import Thread




# Model
model_path = YOLO("C:/Users/phuongta/Desktop/ML/Strawberry_Health/runs/detect/train4/weights/last.pt")
# Stream
cam1_id = 0
cam2_id = 1
# Image
#image_file_path = "C:/Users/phuongta/Desktop/ML/Strawberry_Health/sources/unhealthy/purple_light/leaf4.jpg"

# track object with camera.
#track_objects(model_path, cam2_id)

tracker_thread1 = Thread(target=track_objects, args=(model_path, cam1_id), daemon=True)
tracker_thread2 = Thread(target=track_objects, args=(model_path, cam2_id), daemon=True)

tracker_thread1.start()
tracker_thread2.start()
tracker_thread1.join()
tracker_thread2.join()


"""
# detect object in image
detections = detect_objects_in_image(model_path, image_file_path)
# Process the detections
for class_name, box in detections:
    print(f"Object: {class_name}, Bounding Box: {box}")
"""

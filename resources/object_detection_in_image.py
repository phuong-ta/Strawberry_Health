from ultralytics import YOLO
import cv2


def detect_objects_in_image(model, image_path):
    results = model.predict(source=image_path, show=False, save=True, save_txt=False)
    first_detection = results[0]
    boxes = first_detection.boxes.xyxy.cpu().numpy()
    class_indices = first_detection.boxes.cls.cpu().numpy().astype(int)
    class_names = [model.model.names[i] for i in class_indices]

    detections = []
    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = box
        class_name = class_names[i]
        detections.append((class_name, (x1, y1, x2, y2)))

    return detections

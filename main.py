
# Predict detect bằng Python API
from ultralytics import YOLO

model = YOLO("C:/Users/phuongta/Desktop/ML/Strawberry_Health/runs/detect/train4/weights/last.pt")
source = "C:/Users/phuongta/Desktop/ML/Strawberry_Health/sources/unhealthy/purple_light/leaf4.jpg"
results = model.predict(show=True, save=True, source=source)# source="https://nextcity.org/images/made/219951734_2838e034bb_o_840_630_80.jpg")

#print(results)
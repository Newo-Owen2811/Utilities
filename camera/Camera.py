import cv2
from ultralytics import YOLO

# 1. Load the pre-trained model (it will auto-download the lightweight YOLOv8 nano model)
model = YOLO("yolov8n.pt")

# 2. Open your computer's webcam (0 is usually the built-in webcam)
cap = cv2.VideoCapture(0)

print("Starting camera... Press 'q' on your keyboard to quit.")

while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        print("Could not read from camera.")
        break

    # 3. Run AI object detection on the current camera frame
    results = model(frame)

    # 4. Draw the bounding boxes and labels onto the frame
    annotated_frame = results[0].plot()

    # 5. Display the frame in a popup window
    cv2.imshow("Python Object Detector", annotated_frame)

    # Exit the loop when you press the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up memory and close camera window
cap.release()
cv2.destroyAllWindows()
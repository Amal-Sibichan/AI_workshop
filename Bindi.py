import cv2
import mediapipe as mp
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    if results.pose_landmarks:
                nose = results.pose_landmarks.landmark[0]  # Nose tip
                h, w, _ = frame.shape
                forehead_x = int(nose.x * w)
                forehead_y = int(nose.y * h - 40)  # Move 30 pixels up for forehead

        # Draw a circle on the forehead
                cv2.circle(frame, (forehead_x, forehead_y), 2, (0, 0, 255), -1)
    cv2.imshow('Pose Estimation', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
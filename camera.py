import cv2
import mediapipe as mp
from guess import guess_action

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

actions = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)

    # If person detected
    if result.pose_landmarks:
        actions = ["running" , "monster" , "scared"]

    # After collecting some actions → guess
    if len(actions) > 5:
        guess = guess_action(actions)
        print("🤖 AI Guess:", guess)
        actions.clear()

    cv2.imshow("Charades AI", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
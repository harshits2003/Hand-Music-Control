import cv2
import numpy as np
from hand_tracking import HandTracker
from music_controller import MusicController
from gui import WaveformGUI

# Initialize components
tracker = HandTracker()
music = MusicController("D:/Projects/Music_Control/Hand-Music-Control/music/sample.mp3")
gui = WaveformGUI()

cap = cv2.VideoCapture(0)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        results = tracker.detect_hands(frame)
        tracker.draw_landmarks(frame, results)

        h, w, _ = frame.shape  

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger_tip = hand_landmarks.landmark[8]  # Index finger tip
                thumb_tip = hand_landmarks.landmark[4]         # Thumb tip
                pinky_tip = hand_landmarks.landmark[20]        # Pinky tip
                
                index_x, index_y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
                thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
                pinky_x, pinky_y = int(pinky_tip.x * w), int(pinky_tip.y * h)

                # Volume Control (Hand Distance)
                hand_distance = abs(index_y - thumb_y)
                music.set_volume(hand_distance)

                # Speed Control (Left Hand Pinching)
                left_pinch_distance = abs(thumb_x - index_x)
                speed_factor = np.interp(left_pinch_distance, [10, 100], [0.5, 2.0])
                music.set_speed(speed_factor)

                # Pitch Control (Right Hand Pinching)
                right_pinch_distance = abs(thumb_x - pinky_x)
                pitch_factor = np.interp(right_pinch_distance, [10, 100], [0.5, 2.0])
                music.set_pitch(pitch_factor)

        cv2.imshow("Hand Tracking Music Control", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    gui.stop()

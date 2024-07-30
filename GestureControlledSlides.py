import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cam = cv2.VideoCapture(0)

# Define functions for specific gestures
def perform_zoom_in():
    pyautogui.hotkey('ctrl', '+')

def perform_zoom_out():
    pyautogui.hotkey('ctrl', '-')

def perform_page_up():
    pyautogui.hotkey('shift', ' ')

def perform_page_down():
    pyautogui.press(' ')

# Function to recognize specific gestures based on landmarks
def recognize_gesture(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP].x
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP].y
    index_finger_base = landmarks[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
    thumb_base = landmarks[mp_hands.HandLandmark.THUMB_CMC].x

    fingers_up = [
        index_finger_tip < index_finger_base,
        middle_finger_tip < index_finger_base,
        ring_finger_tip < index_finger_base,
        pinky_tip < index_finger_base
    ]

    # Hand open with fingers extended for zoom in
    if all(fingers_up):
        return 'zoom_in'
    
    # Thumb and index finger in an "L" shape for zoom out
    if thumb_tip > thumb_base and index_finger_tip < index_finger_base and not any(fingers_up[1:]):
        return 'zoom_out'
            
    # Index finger pointing up for page up
    if fingers_up[0] and not any(fingers_up[1:]):
        return 'page_up'
    
    # Index and middle fingers extended (peace sign) for page down
    if fingers_up[0] and fingers_up[1] and not any(fingers_up[2:]):
        return 'page_down'

    return None

# Timer initialization
last_action_time = time.time()
zoom_interval = 0.5 # Time interval in seconds for zoom
action_interval = 2  # Time interval in seconds for page up/down

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Flip frame horizontally for natural reflection
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks.landmark)

            current_time = time.time()

            if gesture == 'zoom_in' and current_time - last_action_time >= zoom_interval:
                perform_zoom_in()
                last_action_time = current_time
            elif gesture == 'zoom_out' and current_time - last_action_time >= zoom_interval:
                perform_zoom_out()
                last_action_time = current_time
            elif gesture == 'page_up' and current_time - last_action_time >= action_interval:
                perform_page_up()
                last_action_time = current_time
            elif gesture == 'page_down' and current_time - last_action_time >= action_interval:
                perform_page_down()
                last_action_time = current_time

    # Display frame
    cv2.imshow('Gesture Controlled Presentation', frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cam.release()
cv2.destroyAllWindows()

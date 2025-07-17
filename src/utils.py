import cv2

def get_finger_position(landmark, width, height):
    return int(landmark.x * width), int(landmark.y * height)

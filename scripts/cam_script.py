#takes photo of hand, can be used for dataset generation

import cv2
import time
import os

def countdown_timer(seconds):
    for second in range(seconds, 0, -1):
        print(f"Capturing in {second} seconds...", end='\r')
        time.sleep(1)
    print("Capturing now!")

def capture_image(capture_folder):
    # Open the webcam (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame from webcam.")
        cap.release()
        return

    # Save the captured image to a file
    timestamp = time.strftime("%Y%m%d%H%M%S")
    image_filename = f"{capture_folder}/captured_image_{timestamp}.jpg"
    cv2.imwrite(image_filename, frame)

    print(f"Image captured and saved as {image_filename}")

    # Release the webcam
    cap.release()

if __name__ == "__main__":
    capture_folder = './captures'
    if not os.path.exists(capture_folder):
        os.makedirs(capture_folder)
    countdown = 1

    print("Press 'q' to quit, or press Enter to capture an image.")

    while True:
        user_input = input()

        if user_input == 'q':
            break
        else:
            countdown_timer(countdown)
            captured_frame = capture_image(capture_folder)

    cv2.destroyAllWindows()
import RPi.GPIO as GPIO
import numpy as np
from ArUcoReader import ArUcoDetector

# Define the GPIO pins
Left_Forward_Pin = 35
Left_Backward_Pin = 31
Right_Forward_Pin = 26
Right_Backward_Pin = 21

#Setting up our pins
GPIO.setmode(GPIO.BOARD)
#Our output pins, start off
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)

# Movement Functions
def forward():
    print("Moving Forward")
    GPIO.output(Left_Forward_Pin, GPIO.HIGH)
    GPIO.output(Left_Backward_Pin, GPIO.LOW)
    GPIO.output(Right_Forward_Pin, GPIO.HIGH)
    GPIO.output(Right_Backward_Pin, GPIO.LOW)

def backward():
    print('backward')
    GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Left motor backward
    GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Right motor backward
    GPIO.output(Left_Backward_Pin, GPIO.LOW) #Left motor off
    GIO.output(Right_Backward_Pin, GPIO.LOW) #Right motor off
    

def turn_left():
    print("Turning Left")
    GPIO.output(Left_Forward_Pin, GPIO.LOW)
    GPIO.output(Left_Backward_Pin, GPIO.HIGH)
    GPIO.output(Right_Forward_Pin, GPIO.HIGH)
    GPIO.output(Right_Backward_Pin, GPIO.LOW)

def turn_right():
    print("Turning Right")
    GPIO.output(Left_Forward_Pin, GPIO.HIGH)
    GPIO.output(Left_Backward_Pin, GPIO.LOW)
    GPIO.output(Right_Forward_Pin, GPIO.LOW)
    GPIO.output(Right_Backward_Pin, GPIO.HIGH)

def stop():
    print("Stopping")
    GPIO.output(Left_Forward_Pin, GPIO.LOW)
    GPIO.output(Left_Backward_Pin, GPIO.LOW)
    GPIO.output(Right_Forward_Pin, GPIO.LOW)
    GPIO.output(Right_Backward_Pin, GPIO.LOW)

if __name__ == "__main__":
    # Load calibration data
    calib_data_path = "/home/pi/Desktop/ArUco_Project/Calib_Data/MultiMatrix.npz"
    calib_data = np.load(calib_data_path)
    cam_mat = calib_data["camMatrix"]
    dist_coef = calib_data["distCoef"]
    marker_size = 7.62  # centimeters

    # Create an instance of ArUcoDetector
    aruco_detector = ArUcoDetector(cam_mat, dist_coef, marker_size)

    def process_marker_data(detector):
        marker_id = 0  # Replace with the actual marker ID you are interested in
        distance = detector.distance(marker_id)
        

        detected_ids = detector.get_ids()
        print(f"Detected marker IDs: {detected_ids}")

    # Start the camera stream with the callback function
    aruco_detector.start_camera_stream(callback=process_marker_data)


import RPi.GPIO as GPIO
import numpy as np
from ArUcoReader import ArUcoDetector
from time import sleep


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

# Set up PWM for motor speed control
Left_Forward_PWM = GPIO.PWM(Left_Forward_Pin, 100)  # 100 Hz frequency
Left_Backward_PWM = GPIO.PWM(Left_Backward_Pin, 100)
Right_Forward_PWM = GPIO.PWM(Right_Forward_Pin, 100)
Right_Backward_PWM = GPIO.PWM(Right_Backward_Pin, 100)

# Start PWM with 0% duty cycle (stopped)
Left_Forward_PWM.start(0)
Left_Backward_PWM.start(0)
Right_Forward_PWM.start(0)
Right_Backward_PWM.start(0)

# Movement Functions
def forward():
    print("Moving Forward")
    Left_Forward_PWM.ChangeDutyCycle(100)  # Full speed
    Left_Backward_PWM.ChangeDutyCycle(0)
    Right_Forward_PWM.ChangeDutyCycle(100)
    Right_Backward_PWM.ChangeDutyCycle(0)

def backward():
    print('backward')
    Left_Backward_PWM.ChangeDutyCycle(100)  # Full speed
    Right_Backward_PWM.ChangeDutyCycle(100)
    Left_Forward_PWM.ChangeDutyCycle(0)
    Right_Forward_PWM.ChangeDutyCycle(0)

def turn_left():
    print("Turning Left")
    Left_Forward_PWM.ChangeDutyCycle(0)
    Left_Backward_PWM.ChangeDutyCycle(50)  # Reduce speed
    Right_Forward_PWM.ChangeDutyCycle(50)  # Reduce speed
    Right_Backward_PWM.ChangeDutyCycle(0)

def turn_right():
    print("Turning Right")
    Left_Forward_PWM.ChangeDutyCycle(25)  # Reduce speed
    Left_Backward_PWM.ChangeDutyCycle(0)
    Right_Forward_PWM.ChangeDutyCycle(0)
    Right_Backward_PWM.ChangeDutyCycle(25)  # Reduce speed

def stop():
    print("Stopping")
    Left_Forward_PWM.ChangeDutyCycle(0)
    Left_Backward_PWM.ChangeDutyCycle(0)
    Right_Forward_PWM.ChangeDutyCycle(0)
    Right_Backward_PWM.ChangeDutyCycle(0)



if __name__ == "__main__":
    # Load calibration data
    calib_data_path = "/home/pi/Desktop/Calib_Data/MultiMatrix.npz"
    calib_data = np.load(calib_data_path)
    cam_mat = calib_data["camMatrix"]
    dist_coef = calib_data["distCoef"]
    marker_size = 7.62  # centimeters
    

    
    # Create an instance of ArUcoDetector
    aruco_detector = ArUcoDetector(cam_mat, dist_coef, marker_size)
    
    global counter
    counter = 0
    
    def process_marker_data(detector):
        marker_id = 1  # Replace with the actual marker ID you are interested in
        distance = detector.distance(marker_id)
        orientation = detector.orientation(marker_id)  # Get the orientation of the marker
        global counter
        
        if distance is not None and orientation is not None:
            print(f"Distance to marker {marker_id}: {distance:.2f} cm")
            print(f"Orientation to marker {marker_id}: {orientation:.2f} degrees")
            if abs(90-abs(orientation)) <= 1 :  # Check if the rover is facing the marker head-on (within 5 degrees)
                counter += 1
                stop()
            #elif orientation > 0:
            #    turn_left()  # Adjust to the left
            #elif orientation < 0:
            #    turn_right()  # Adjust to the right
            if distance >= 25.4 and counter > 0:
                forward()
            elif distance < 25.4 and counter > 0:
                stop()
        elif counter <= 0:
            print(f"Marker {marker_id} not detected")
            turn_right()  # Turn right to search for the marker
            print(counter)
        else:
            print(f"Marker {marker_id} not detected")
            stop()

        detected_ids = detector.get_ids()
        print(f"Detected marker IDs: {detected_ids}")

    # Start the camera stream with the callback function
    aruco_detector.start_camera_stream(callback=process_marker_data)
    
    GPIO.output(Left_Forward_Pin, GPIO.LOW)
    GPIO.output(Left_Backward_Pin, GPIO.LOW)
    GPIO.output(Right_Forward_Pin, GPIO.LOW)
    GPIO.output(Right_Backward_Pin, GPIO.LOW)
    GPIO.cleanup()
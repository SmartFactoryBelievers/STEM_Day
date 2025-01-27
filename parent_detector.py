from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
from time import sleep

PIR_PIN = 18 #the internal Pi pin number


#Setting up our pins
#GPIO.setmode(GPIO.BOARD)
#Our output pins, start off
#GPIO.setup(PIR_PIN, GPIO.OUT, initial=GPIO.HIGH)

#setup components
pir = MotionSensor(PIR_PIN) #setup PIR sensor
cam = PiCamera() #setup camera
filename = "{0:%Y}-{0:%m}-{0:%d}".format(datetime.now())
#print(str(filename))

#set camera resolution
cam.resolution = (640, 480)

# Change the rate at which the camera records images
cam.framerate = 30

# Rotate the image by x degrees
# Note that the camera assembly is upside down so 180 is right side up
# For challenge 3, try other rotation angles
cam.rotation = 90

#test PIR sensor
#print("waiting for motion")
#pir.wait_for_motion()
#print("Motion detected!")


#main block
while True:
    print("waiting for motion...")
    
    #preview motion
    pir.wait_for_motion() #detect motion
    print("Motion detected!")
    cam.start_preview() #start camera when motion detected
    sleep(5)
    pir.wait_for_no_motion() #detect lack of motion
    cam.stop_preview() #stop camera when no motion
    
    '''
    #record motion
    pir.wait_for_motion() #detect motion
    print("Motion detected!")
    cam.start_recording(str(filename),format='mjpeg') #record motion
    pir.wait_for_no_motion() #detect lack of motion
    cam.stop_recording() #stop camera when no motion
'''

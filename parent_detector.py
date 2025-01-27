from gpiozero import MotionSensor
from picamzero import Camera
from datetime import datetime

#setup components
pir = MotionSensor(4) #setup PIR sensor
cam = Camera() #setup camera
filename = "{0:%Y}-{0:%m}-{0:%d}".format(datetime.now())

''' #test PIR sensor
pir.wait_for_motion()
print("Motion detected!")
'''

#main block
while True:
    pir.wait_for_motion() #detect motion
    print("Motion detected!")
    cam.start_preview() #start camera when motion detected
    cam.start_recording(str(filename)+".mp4") #record motion
    pir.wait_for_no_motion() #detect lack of motion
    cam.stop_preview() #stop camera when no motion
    '''cam.stop_recording() '''


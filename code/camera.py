from picamera import PiCamera
from time import sleep

camera = PiCamera()

# the code below is for recording
camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()

# the code below is for pictures (comment out one section to use the other [//] [#])
#camera.start_preview() 
#sleep(10)
#camera.capture('locations')
#camera.stop_preview()

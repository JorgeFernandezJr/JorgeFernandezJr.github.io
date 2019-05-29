from picamera import PiCamera
from time import sleep

camera = PiCamera()

# the code below is for recording
camera.start_preview()
camera.start_recording('/home/pi/video_name.h001')
sleep(10)
camera.stop_recording()
camera.stop_preview()
#to play the recorded video omxplayer video_name.h001
----------------------------------------------------------------------------------------------------------
# the code below is for pictures (comment out one section to use the other [//] [#])
#camera.start_preview() 
#sleep(10)
#camera.capture('locations')
#camera.stop_preview()

-----------------------------------------------------------------------------------------------------------

#MATERIALS:
#Raspberry Pi Zero Wireless × 1 
#Amazon Affiliate Link - https://goo.gl/Zsxm7k

#Raspberry Pi Camera module × 1
#Amazon Affiliate Link - https://goo.gl/4kR632

#Check out the NoIR camera for night surveillance (not needed)
#Amazon Affiliate Link - https://goo.gl/fT7oL9

#Raspberry Pi Zero Camera Cable x 1
#Amazon Affiliate Link - https://goo.gl/pBVZb1
 
#Micro-USB to USB Cable × 1 
#1/4" MDF Board × 1 
#90 Degree Angle Bracket × 1 
#Outdoor Mounting Tape × 1 
#M4 X 20mm Long Machine Screws × 2 
#M4 Hex Nuts × 2 
#M2.5 Machine Screws × 4 
#8 X 3/4" Long Machine Screws × 1 
#8 Hex Nut × 1 
#8 Wing Nut × 1 

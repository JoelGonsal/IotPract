import time
import picamera
camera = picamera.PiCamera()
camera.resolution=(1080,720)
camera.start_preview()
time.sleep(10)
camera.capture('test.png')
camera.stop_preview()

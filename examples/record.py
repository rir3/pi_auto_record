from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start_and_record_video("video.mp4", duration=5)
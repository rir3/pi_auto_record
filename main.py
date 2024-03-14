from gpiozero import Button
from picamera2 import Picamera2
import subprocess

#Relay Activated Auto Recording
#This program will start recording when Pin 11 GPIO 17 is grounded.
#This can be activated with a relay.

#Resources
dir = 'shared/'
video = 'video.mp4'
image = 'logo.png'
output_video = 'output_video.mp4'
recording_duration = 10

#Trigger
button = Button(17)
print("Waiting for button press.")
button.wait_for_press()
print("The button was pressed!")


#Record
picam2 = Picamera2()
picam2.start_and_record_video(video, duration=recording_duration)

#Logo Embeding
ffmpeg_command = [
    'ffmpeg',
    '-i', video,
    '-i', image,
    '-filter_complex', '[1:v]scale=250:-1[logo];[0:v][logo]overlay=W-w-10:H-h-10',
    '-c:a', 'copy',
    output_video
]
process = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if process.returncode == 0:
    print("FFmpeg command executed successfully")
else:
    print(f"FFmpeg command failed with error: {process.stderr.decode('utf-8')}")


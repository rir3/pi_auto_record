from gpiozero import Button
from picamera2 import Picamera2
import subprocess
from datetime import datetime
import logging

#Relay Activated Auto Recording
#This program will start recording when Pin 11 GPIO 17 is grounded.
#This can be activated with a relay.

#Resources
dir = '/home/pi/Projects/pi_auto_record/IllusionistVideos/'
video = '/home/pi/Projects/pi_auto_record/video.mp4'
image = '/home/pi/Projects/pi_auto_record/logo.png'
recording_duration = 10

def main():
    #Resources
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_video = f"output_video_{timestamp}.mp4"

    #Trigger
    button = Button(17)
    logging.info("Waiting for button press.")
    button.wait_for_press()
    logging.info("The button was pressed!")


    #Record
    logging.info("Recording Started.")
    picam2 = Picamera2()
    picam2.start_and_record_video(video, duration=recording_duration)
    picam2.close()

    #Logo Embeding
    logging.info("Logo Embeding Started.")
    ffmpeg_command = [
        'ffmpeg',
        '-i', video,
        '-i', image,
        '-filter_complex', '[1:v]scale=250:-1,vflip[logo];[0:v][logo]overlay=W-w-10:H-h-10',
        '-c:a', 'copy',
        dir+output_video
    ]
    process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()

    if process.returncode == 0:
        print("FFmpeg command executed successfully")
    else:
        print(f"FFmpeg command failed with error: {process.stderr.read().decode('utf-8')}")
        #raise Exception(f"FFmpeg command failed with error: {process.stderr.read().decode('utf-8')}")

if __name__ == "__main__":
    main()
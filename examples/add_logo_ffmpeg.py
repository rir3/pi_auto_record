import subprocess

# Define your FFmpeg command
ffmpeg_command = [
    'ffmpeg',
    '-i', './video.mp4',
    '-i', './logo.png',
    '-filter_complex', '[1:v]scale=250:-1[logo];[0:v][logo]overlay=W-w-10:H-h-10',
    '-c:a', 'copy',
    './output_video.mp4'
]

# Run the FFmpeg command
process = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Check if the process was successful
if process.returncode == 0:
    print("FFmpeg command executed successfully")
else:
    print(f"FFmpeg command failed with error: {process.stderr.decode('utf-8')}")

import ffmpeg

input_video = ffmpeg.input('video.mp4')
input_logo = ffmpeg.input('logo.png')

# Scale the logo to desired dimensions
logo_scaled = input_logo.filter('scale', 250, -1)

# Overlay the scaled logo onto the input video
output_video = ffmpeg.overlay(input_video, logo_scaled, x='W-w-10', y='H-h-10')

# Output the resulting video without stream copying
output_video = output_video.output('output_video2.mp4')

# Run the ffmpeg command and capture stderr
try:
    ffmpeg.run(output_video, capture_stderr=True)
except ffmpeg.Error as e:
    if e.stderr:
        print('stderr:', e.stderr.decode('utf-8'))

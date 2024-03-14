import cv2

# Load the video
video_path = 'video.mp4'
cap = cv2.VideoCapture(video_path)

# Load the overlay image
overlay_path = 'logo.png'
overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)

# Get the width and height of the overlay image
overlay_height, overlay_width, _ = overlay.shape

# Set the desired size for the overlay
new_overlay_height = 200
new_overlay_width = 200

# Resize the overlay image
overlay = cv2.resize(overlay, (new_overlay_width, new_overlay_height))

# Get the width and height of the video
video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a VideoWriter object to write the output video
output_path = 'output_video.mp4'
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
out = cv2.VideoWriter(output_path, fourcc, fps, (video_width, video_height))

# Loop through each frame of the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Overlay the PNG image onto the frame at the bottom right corner
    overlay_x = video_width - new_overlay_width
    overlay_y = video_height - new_overlay_height
    roi = frame[overlay_y:overlay_y + new_overlay_height, overlay_x:overlay_x + new_overlay_width]

    # Blend the overlay with the frame
    for c in range(0, 3):
        roi[:, :, c] = overlay[:, :, c] * (overlay[:, :, 3] / 255.0) + roi[:, :, c] * (1.0 - overlay[:, :, 3] / 255.0)

    # Write the modified frame to the output video
    out.write(frame)

# Release resources
cap.release()
out.release()

import cv2
import sys
import os

# --- CONFIGURATION ---
input_video = "task2.mp4"   # <-- change this to your input video filename
output_video = "gray_" + os.path.basename(input_video)

# --- OPEN VIDEO ---
cap = cv2.VideoCapture(input_video)
if not cap.isOpened():
    print(f"Error: Could not open video {input_video}")
    sys.exit()

# --- GET VIDEO INFO ---
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec
fps = cap.get(cv2.CAP_PROP_FPS)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# --- CREATE OUTPUT VIDEO WRITER ---
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height), isColor=False)

# --- PROCESS FRAMES ---
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(gray)

# --- CLEANUP ---
cap.release()
out.release()
print(f"✅ Grayscale video saved as: {output_video}")

# ==============================================
# 🧩 Combine Two Videos Side-by-Side (Auto Resize)
# Author: ChatGPT
# ==============================================

import cv2
import numpy as np
import os

# -------------------------------
# 🔧 Input and Output Paths
# -------------------------------
video1_path = "input.mp4"   # ← your first video
video2_path = "t2.mp4"           # ← your second video
output_path = "combined_side_by_side.mp4"

# -------------------------------
# 🎬 Open both videos
# -------------------------------
cap1 = cv2.VideoCapture(video1_path)
cap2 = cv2.VideoCapture(video2_path)

if not cap1.isOpened():
    print(f"❌ Error: Could not open {video1_path}")
    exit()
if not cap2.isOpened():
    print(f"❌ Error: Could not open {video2_path}")
    exit()

# -------------------------------
# 📏 Get properties
# -------------------------------
fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)
fps = min(fps1, fps2)  # use lower FPS to sync playback

width1, height1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
width2, height2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Determine common height for alignment
final_height = min(height1, height2)

# Compute new widths keeping aspect ratio
new_width1 = int(width1 * final_height / height1)
new_width2 = int(width2 * final_height / height2)

final_width = new_width1 + new_width2

# -------------------------------
# 💾 VideoWriter for output
# -------------------------------
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (final_width, final_height))

print("🚀 Combining videos (auto resizing)... please wait")

# -------------------------------
# 🔁 Process frames
# -------------------------------
while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not (ret1 and ret2):
        break

    # Resize both frames
    frame1_resized = cv2.resize(frame1, (new_width1, final_height))
    frame2_resized = cv2.resize(frame2, (new_width2, final_height))

    # Combine side-by-side
    combined_frame = np.hstack((frame1_resized, frame2_resized))

    out.write(combined_frame)

# -------------------------------
# ✅ Cleanup
# -------------------------------
cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()

print(f"✅ Done! Combined video saved as: {os.path.abspath(output_path)}")

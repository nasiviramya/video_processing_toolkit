# ==============================================
# 🧩 Combine Two Videos Side-by-Side (No Resize)
# Author: ChatGPT
# ==============================================

import cv2
import numpy as np
import os

# -------------------------------
# 🔧 Input and Output Paths
# -------------------------------
video1_path = "task2x.mp4"   # ← change to your first video
video2_path ="color_on_bw_video.mp4"   # ← change to your second video
output_path = "customplot_and_plot_overlay_combained_side_by_side.mp4"  # output file name

# -------------------------------
# 🎬 Open both video files
# -------------------------------
cap1 = cv2.VideoCapture(video1_path)
cap2 = cv2.VideoCapture(video2_path)

# ✅ Check if both videos opened successfully
if not cap1.isOpened():
    print(f"❌ Error: Could not open {video1_path}")
    exit()
if not cap2.isOpened():
    print(f"❌ Error: Could not open {video2_path}")
    exit()

# -------------------------------
# 📏 Get video properties
# -------------------------------
fps = int(cap1.get(cv2.CAP_PROP_FPS))
width = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Check if both videos have same size
width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

if width != width2 or height != height2:
    print("❌ Error: Videos must be the same width and height!")
    cap1.release()
    cap2.release()
    exit()

# -------------------------------
# 💾 Create VideoWriter for output
# -------------------------------
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width * 2, height))

print("🚀 Combining videos... please wait")

# -------------------------------
# 🔁 Process each frame
# -------------------------------
while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not (ret1 and ret2):
        break  # Stop when either video ends

    # Combine frames side by side
    combined_frame = np.hstack((frame1, frame2))

    # Write to output
    out.write(combined_frame)

    # Optional: live preview
    # cv2.imshow("Combined", combined_frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# -------------------------------
# ✅ Cleanup
# -------------------------------
cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()

print(f"✅ Done! Combined video saved as: {os.path.abspath(output_path)}")

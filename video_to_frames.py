from moviepy.editor import VideoFileClip
import numpy as np

def video_to_frames(video_file: str, interval: int = 1) -> [np.ndarray]:
  clip = VideoFileClip(video_file)
  frames = []
  duration = clip.duration
  fps = clip.fps
  
  for t in range(0, int(duration), interval):
    frame = clip.get_frame(t)
    frames.append(frame)
    
  return frames


if __name__ == "__main__":
  video_file = 'testout.mp4'
  frames = video_to_frames(video_file)
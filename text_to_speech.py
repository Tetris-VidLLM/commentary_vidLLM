from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioClip, AudioFileClip, concatenate_audioclips
import numpy as np

def make_blank_frame(t):
  numpy_array = np.array([0,0])
  return numpy_array

def text_to_mp3(text, outfile_name):
  # Create a gTTS object
  tts = gTTS(text=text, lang="en", slow=False)
  tts.save(outfile_name)

def add_mp3_to_mp4(mp4file, mp3file, outfile):
  vid_clip = VideoFileClip(mp4file)
  audio_clip = AudioFileClip(mp3file)

  if audio_clip.duration < vid_clip.duration:
      # Calculate the duration of the required blank audio clip
      blank_duration = vid_clip.duration - audio_clip.duration
      # Create a blank audio clip with the required duration
      blank_audio = AudioClip(make_blank_frame, duration=blank_duration)
      # Concatenate the generated audio with the blank audio
      final_audio = concatenate_audioclips([audio_clip, blank_audio])
  else:
      # If the audio duration is longer, trim it to match the video duration
      final_audio = audio_clip.subclip(0, vid_clip.duration)

  video_with_audio = vid_clip.set_audio(final_audio)
  video_with_audio.write_videofile(outfile)

def add_ttl_to_video(mp4file, text, outfile):
  tmp_mp3_filename = 'tmp.mp3'
  text_to_mp3(text, tmp_mp3_filename)
  add_mp3_to_mp4(mp4file, tmp_mp3_filename, outfile)

if __name__ == "__main__":
  text = "Texas she beat at her husband in the finals to get the free trip to Portland which I'm sure will be bragging rights for the lifetime big Tetris for Kristen to start things off this is Paul Teddy's first top 30 to finish he's got the headphones in he's dialed in as you can see Kristen competed in the 2014 tournament and this is the first time she has returned to the CTW"
  add_ttl_to_video("data/30clip/clips/video_0_1.mp4",text, 'testout.mp4')

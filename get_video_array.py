from pytube import YouTube 
import moviepy.editor as mp
from moviepy.editor import VideoFileClip

# Where to save  
SAVE_PATH = "./videos/"  # to_do
RESOLUTION = "360p"

def split_video(input_file, clip_durations, output_prefix: str = SAVE_PATH + "clip"):
    video = VideoFileClip(input_file)
    total_duration = video.duration

    current_time = 0
    index = 1
    clip_file_paths = []
    for clip_duration in clip_durations:
        if current_time < total_duration:
            end_time = min(current_time + clip_duration, total_duration)
            clip = video.subclip(current_time, end_time)
            clip_file = f"{output_prefix}_{index}.mp4"
            clip_file_paths.append(clip_file)
            clip.write_videofile(clip_file)
            print(f"Created {clip_file}")
            current_time = end_time
            index += 1

    video.close()
    return clip_file_paths

def get_mp4(video_link: str, filename: str = SAVE_PATH + "video.mp4", resolution: int = RESOLUTION):
    try:
        yt = YouTube(video_link)  
    except:
        return None
    
    # Filters out all the files with "mp4" extension  
    mp4files = yt.streams.filter(progressive=True, file_extension='mp4')
    to_download = mp4files.get_by_resolution(resolution)
    if to_download is None:
        to_download = mp4files.order_by('resolution')[0]
    try:
        to_download.download(filename=filename + ".mp4")
        return filename + ".mp4"
    except:
        return None

def mp4_to_array(mp4_file):
    try:
        video_clip = mp.VideoFileClip(mp4_file)
        video_array = video_clip.get_frame(0)  # Extracting the first frame as an array
        video_clip.close()  # Close the video clip
        return video_array
    except:
        return None

if __name__ == "__main__":
    mp4_file = get_mp4("https://www.youtube.com/watch?v=fYyDQBG_tYc&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=1", SAVE_PATH + "2018_round0.mp4")
    if mp4_file is not None:
        video_array = mp4_to_array(mp4_file)
        print(video_array)
    else:
        print("Failed to download the video.")

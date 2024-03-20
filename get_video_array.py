from pytube import YouTube 
import moviepy.editor as mp
from moviepy.editor import VideoFileClip

# Where to save  
SAVE_PATH = "./videos/"  # to_do
RESOLUTION = "360p"

def split_video(input_file, transcript_jsons, output_prefix: str = SAVE_PATH + "clip", min_clip_duration=0):
    video = VideoFileClip(input_file)
    total_duration = video.duration
    clip_index = 0
    transcript_idx = 0
    clip_file_paths = []
    clip_durations = []
    clip_texts = []
    while transcript_idx < len(transcript_jsons):
        cur_clip_text = transcript_jsons[transcript_idx]['text']
        cur_clip_start = transcript_jsons[transcript_idx]['start']
        cur_clip_end =  transcript_jsons[transcript_idx]['start'] + transcript_jsons[transcript_idx]['duration']
        while cur_clip_end - cur_clip_start < min_clip_duration and transcript_idx < len(transcript_jsons) - 1:
            transcript_idx += 1
            cur_clip_text += " " + transcript_jsons[transcript_idx]['text']
            cur_clip_end = transcript_jsons[transcript_idx]['start'] + transcript_jsons[transcript_idx]['duration']
        cur_clip_end = min(cur_clip_end, total_duration)
        if cur_clip_end - cur_clip_start >= min_clip_duration:
            clip = video.subclip(cur_clip_start, cur_clip_end)
            clip_file = f"{output_prefix}_{clip_index}.mp4"
            clip_file_paths.append(clip_file)
            clip_durations.append(clip.duration)
            clip_texts.append(cur_clip_text)
            clip.write_videofile(clip_file)
            print(f"Created {clip_file}")
            clip_index += 1
        transcript_idx += 1

    video.close()
    return clip_file_paths, clip_durations, clip_texts

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

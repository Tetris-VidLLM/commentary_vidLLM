import json
import multiprocessing

from get_transcript import get_transcript
from get_video_array import get_mp4, split_video
from utils import make_directory_if_not_exists


VIDEO_LINKS = [
  "https://www.youtube.com/watch?v=fYyDQBG_tYc&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=1&pp=iAQB",
  "https://www.youtube.com/watch?v=KBpUUQ6lGJY&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=2&pp=iAQB",
  "https://www.youtube.com/watch?v=ZK55M0yoHbw&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=3&pp=iAQB",
  "https://www.youtube.com/watch?v=z6BAse-T5qU&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=4&pp=iAQB",
  "https://www.youtube.com/watch?v=emynrB4I0Ug&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=5&pp=iAQB",
  "https://www.youtube.com/watch?v=dqir7p4pVs8&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=6&pp=iAQB",
  "https://www.youtube.com/watch?v=NC-d-mVYECY&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=7&pp=iAQB",
  "https://www.youtube.com/watch?v=YsAbgm_q4z4&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=8&pp=iAQB",
  "https://www.youtube.com/watch?v=4NCmRwm0enM&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=9&pp=iAQB",
  "https://www.youtube.com/watch?v=u0x3qpO2iC4&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=10&pp=iAQB", 
  "https://www.youtube.com/watch?v=0xjQeMC1Vsc&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=11&pp=iAQB",
  "https://www.youtube.com/watch?v=YNZsCJkrt8U&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=12&pp=iAQB",
  "https://www.youtube.com/watch?v=L_UPHsGR6fM&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=13&pp=iAQB"
]

OUTFILE_PATH_PREFIX = "./data/0clip/"
MULTIPROCESS = True
MIN_CLIP_DURATION = 0

def video_to_data(video_link: str, data_file_prefix: str, data_outfile: str):
  transcript = get_transcript(video_link)
  if transcript is None:
    return
  video_mp4 = get_mp4(video_link, OUTFILE_PATH_PREFIX + "videos/full_" + data_file_prefix)
  if video_mp4 is None:
    return
  out_json = []
  clip_filenames, clip_durations, clip_texts = split_video(video_mp4, transcript, OUTFILE_PATH_PREFIX + "clips/" + data_file_prefix, MIN_CLIP_DURATION)
  for i in range(len(clip_filenames)):
    out_json.append({"duration": clip_durations[i], "clip_filename": clip_filenames[i], "target_text": clip_texts[i]})
  with open(data_outfile, "w") as json_file:
    json.dump(out_json, json_file)


if __name__ == "__main__":
  make_directory_if_not_exists(OUTFILE_PATH_PREFIX)
  make_directory_if_not_exists(OUTFILE_PATH_PREFIX+"videos/")
  make_directory_if_not_exists(OUTFILE_PATH_PREFIX+"clips/")
  make_directory_if_not_exists(OUTFILE_PATH_PREFIX+"training/")

  if MULTIPROCESS:
    processes = []
    for i, video_link in enumerate(VIDEO_LINKS):
      process = multiprocessing.Process(target=video_to_data, args=(video_link, f"video_{i}", OUTFILE_PATH_PREFIX+"training/" + f"video_{i}.json"))
      processes.append(process)
      process.start()
    for process in processes:
      process.join()
  else:
    for i, video_link in enumerate(VIDEO_LINKS):
      video_to_data(video_link, f"video_{i}", OUTFILE_PATH_PREFIX+"training/" + f"video_{i}.json")
from pytube import YouTube 
  
#where to save  
SAVE_PATH = "./videos/" #to_do
RESOLUTION = "360p"
  
def get_mp4(video_link: str, filename: str):
  try:
    yt = YouTube(video_link)  
  except:
    return None
    
  # filters out all the files with "mp4" extension  
  mp4files = yt.streams.filter(progressive=True, file_extension='mp4')
  to_download = mp4files.get_by_resolution(RESOLUTION)
  if to_download is None:
    to_download = mp4files.order_by('resolution')[0]
  try:
    to_download.download(output_path=SAVE_PATH, filename=filename)
    return to_download.title
  except:
    return None

if __name__ == "__main__":
  srt = get_mp4("https://www.youtube.com/watch?v=fYyDQBG_tYc&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=1", "2018_round0.mp4")
  print(srt)
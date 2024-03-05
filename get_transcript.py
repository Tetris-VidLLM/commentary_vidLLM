from youtube_transcript_api import YouTubeTranscriptApi 
import re

def get_transcript(youtube_link: str):
  pattern = re.compile(r'\?v=([^&]+)')
  match = pattern.search(youtube_link)
  if match:
    srt = YouTubeTranscriptApi.get_transcript(match.group(1), languages=['en'])
    return srt
  return []

if __name__ == "__main__":
  srt = get_transcript("https://www.youtube.com/watch?v=fYyDQBG_tYc&list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ&index=1")
  print(srt)
import ytdown
import requester
import info_extracter
import tts
if __name__=="__main__":
    ytdown.downloader("https://www.youtube.com/watch?v=L_UPHsGR6fM")
    info_extracter.extract_info_from_frames()
    text=requester.requester()
    tts.add_ttl_to_video("./tmp/output.mp4",text, './output_with_commentary.mp4')
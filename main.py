import dowloader
import uploader
import getclips
import os, shutil
import time
import Video
import datetime
from moviepy.editor import *




def main():
    #url = input("clip: ")
    

    ULRs = getclips.get_Clips_Urs()
    if (len(ULRs) >= 6):
        for i in range(6):
            if(os.path.exists("clip.mp4")):
                os.remove("clip.mp4")
            
            url = ULRs[i]
            clip_info = dowloader.get_info(url)
            dowloader.download_clip(url)
            clip1 = VideoFileClip("clip.mp4")
            video = Video.Video.createVideo(clip1)
            video.write_videofile("clip_edit.mp4")
            #os.rename("clip_edit.mp4","clip" + str(i) + ".mp4" )
            #shutil.move("clip" + str(i)  + ".mp4","data/clip" + str(i)  + ".mp4")


            video_data = {
            "file": "clip_edit.mp4",
            "title": clip_info['data'][0]['title'] + " #shorts ",
            "description": "Ein clip von " + clip_info['data'][0]['broadcaster_name'],
            "keywords":"twitch,twitch Clips," + clip_info['data'][0]['broadcaster_name'],
            "privacyStatus":"private" }
            uploader.upload_video(video_data)


uploaded = False

if __name__ == '__main__':
    while True:
        current_time = datetime.datetime.now()
        
        if(not uploaded and current_time.hour == 0):
            main()
            uploaded = True

        if(current_time.hour == 23):
            uploaded = False
        time.sleep(10000)


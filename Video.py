# This class deals with the formatting and editing of the video before uploading.
from moviepy.editor import *
from moviepy.editor import VideoFileClip, AudioFileClip
import time
from tqdm import tqdm



class Video:
    def __init__(self, dir, caption, user):
        self.dir = dir
        try:
            self.clip = VideoFileClip(self.dir)
        except Exception as e:
            print(f"Could not convert {self.dir} into a video file")
            print(f"Error: {e}")
            self.clip = None
        self.font = "Arial"
        self.font_size = 80
        self.caption = caption
        self.tiktok_dim = (1080, 1920)
        self.bg = "black"
        self.color = "white"
        self.userPreference = user



    def createVideo(clip, direct=False):
        clip = clip.resize(width=1080)  # Ignore error.
        base_clip = ColorClip(size=(1080, 1920), color=[10, 10, 10], duration=clip.duration)
        OFFSET = -20
        bottom_meme_pos = 960 + (((1080 / clip.size[0]) * (clip.size[1])) / 2) + OFFSET
        # top_meme_pos = 960 - (((1080 / self.clip.size[0]) * (self.clip.size[1])) / 2) - OFFSET
        # to_pos = 1920 / 6
        

        clip = CompositeVideoClip([base_clip, clip.set_position(("center", "center"))])
        # Continue normal flow.
        return clip
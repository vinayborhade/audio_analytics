# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:24:50 2020

@author: Vinay Borhade
"""

from Video import Video_Obj

video_path = "/video/"
video_filename = "An Introduction to Linear Regression Analysis.mp4"
video_file = video_path + video_filename

video_obj = Video_Obj(video_file)
audio_path = "/audio/"
audio_filename = video_obj.extract_audio(audio_path)
print(audio_filename)

audio_file = audio_path + audio_filename
audio_obj = Audio_Object(audio_file)
text_path = "/text/"
text_filename = audio_obj.extract_text(text_path)
print(text_filename)

text_file = text_path + text_filename
text_obj = Text_Object(text_file)
text_obj.extract_features()
text_obj.pre_process()



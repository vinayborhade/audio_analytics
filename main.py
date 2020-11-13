# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:24:50 2020

@author: Vinay Borhade
"""

from Video import Video_Obj
from Audio import Audio_Object
from Text import Text_Object

video_file_path = "./video/"
video_filename = "An Introduction to Linear Regression Analysis"
video_extn = ".mp4"
video_file = video_file_path + video_filename + video_extn
video_obj = Video_Obj(video_file_path, video_filename, video_extn)

audio_path = "./audio/"
audio_filename = video_obj.extract_audio(audio_path)
print(audio_filename)

audio_path = "./audio/"
audio_filename = video_filename
audio_extn = ".wav"

audio_obj = Audio_Object(audio_path, audio_filename, audio_extn)

# chunking to be done only once for an audio file; hence commented
audio_obj.chunk()

text_path = "./text/"
text_filename = video_filename
text_extn = ".xlsx"
text_file = text_path + text_filename + text_extn
text_obj = Text_Object(text_file)

print(text_obj.text_df)

text_obj.extract_features()
text_obj.pre_process()



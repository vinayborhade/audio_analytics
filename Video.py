# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:24:50 2020

@author: Vinay Borhade
"""
#pip install moviepy

import moviepy.editor as mpe

class Video_Obj(object):
    
    def __init__(self, video_file_path, video_filename, video_extn):
        self.video_file_path = video_file_path
        self.video_filename = video_filename
        self.video_extn = video_extn
        
        self.video_stream = mpe.VideoFileClip(self.video_file_path + 
                                              self.video_filename +
                                              self.video_extn)
        
    def extract_audio(self, audio_path):
        print('In Video_Obj.extract_audio')
        
        self.audio_path = audio_path
        self.audio_filename = self.video_filename
        self.audio_extn = '.wav'
        
        audio_file = self.audio_path +self.audio_filename + self.audio_extn
        
        # code for extracting audio and saving
        self.video_stream.audio.write_audiofile(audio_file)
        
        return(audio_file)
        
if __name__ == "__main__":
    video_file_path = "./video/"
    video_filename = "An Introduction to Linear Regression Analysis"
    video_extn = ".mp4"
    video_file = video_file_path + video_filename + video_extn
    video_obj = Video_Obj(video_file_path, video_filename, video_extn)
    
    audio_path = "./audio/"
    audio_filename = video_obj.extract_audio(audio_path)
    print(audio_filename)
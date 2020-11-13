# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:24:50 2020

@author: Vinay Borhade
"""
#pip install SpeechRecognition
#pip install pydub

import os 
import glob
import pandas as pd
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_nonsilent

class Audio_Object(object):
    
    def __init__(self, audio_path, audio_filename, audio_extn):
        self.audio_path = audio_path
        self.audio_filename = audio_filename
        self.audio_extn = audio_extn
        
        self.audio_stream = sr.AudioFile(self.audio_path + 
                                              self.audio_filename +
                                              self.audio_extn)
                                         
        self.chunk_path = self.audio_path + "chunks"    
        self.whole_text= ""  
        self.ts = None
        
        self.text_path = "./text/"
        self.text_filename = audio_filename
        self.text_extn = ".xlsx"

    @classmethod
    def extract_text(cls, filename):
        print('In Audio_Object.extract_text')
        ''' Extract the text from audio '''
        r = sr.Recognizer()
        text = ""
        
        # recognize the chunk
        with sr.AudioFile(filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(filename, ":", text)
                
        return(text)                          
    
    def get_filenames_in_chunk_folder(self):
        filenames = glob.glob(self.chunk_path+"/*.wav")
        return(filenames)
        
    def extract_text_from_chunk_folder(self):
        for filename in self.get_filenames_in_chunk_folder():
            self.whole_text += Audio_Object.extract_text(filename)
            
    def save_ts_df(self):
        self.ts.to_excel(self.text_path + 
                         self.text_filename +
                         self.text_extn)
                                     
    def chunk(self):
        print('In Audio_Object.Chunk')
        ''' Chunk the audio in smaller files and save to chunk_path '''
        
        # open the audio file using pydub
        sound = AudioSegment.from_wav(self.audio_path + 
                                              self.audio_filename +
                                              self.audio_extn)
    
        silence_to_keep = 100
        # split audio sound where silence is 700 miliseconds or more and get chunks
        chunks = split_on_silence(sound,
            # experiment with this value for your target audio file
            min_silence_len = 700,
            # adjust this per requirement
            silence_thresh = sound.dBFS-14,
            # keep the silence for 1 second, adjustable as well
            keep_silence=silence_to_keep,
        )
        
        # create a directory to store the audio chunks
        if not os.path.isdir(self.chunk_path):
            os.mkdir(self.chunk_path)
            
        times = []
        #Print detected non-silent chunks, which in our case would be spoken words.
        nonsilent_data = detect_nonsilent(sound, min_silence_len=700, silence_thresh=sound.dBFS-14, seek_step=1)
        
        #convert ms to seconds
        print("start,Stop")
        for chunks_times in nonsilent_data:
            times.append( [ct/1000 for ct in chunks_times])
            
        self.ts = pd.DataFrame(times, columns=["start_time", "stop_time"])
        
        # print(self.ts.head())
        
        # process each chunk 
        
        dur_sec = []
        text = []
        
        for i, audio_chunk in enumerate(chunks, start=1):
            # export audio chunk and save it in
            # the `folder_name` directory.
            chunk_filename = os.path.join(self.chunk_path, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            
            dur_sec.append(audio_chunk.duration_seconds - 
                           ((silence_to_keep*2)/1000))
            text.append(Audio_Object.extract_text(chunk_filename))
        # return the text for all chunks detected
        # return(self.whole_text)
    
        self.ts['duration'] = dur_sec
        self.ts['text'] = text
        self.ts['label'] = self.audio_filename
        self.save_ts_df()
    
if __name__ == "__main__":
    audio_path = "./audio/"
    audio_filename = "An Introduction to Linear Regression Analysis"
    audio_extn = ".wav"

    audio_obj = Audio_Object(audio_path, audio_filename, audio_extn)
    
    # chunking to be done only once for an audio file; hence commented
    audio_obj.chunk()
    
    # audio_obj.extract_text_from_chunk_folder()
    
    # audio_obj.whole_text
    
    

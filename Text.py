# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:24:50 2020

@author: Vinay Borhade
"""

class Text_Object(object):
    def __init__(self, file):
        self.text_file = file
        self.models = []
        
    def extract_features(self):
        print('In Text_Object.extract_features')
    
    def pre_process(self):
        print('In Text_Object.pre_process')

    # def register_models(self, model):
    #     self.models.append(model)
        
        
if __name__ == "__main__":
    text_path = "/text/"
    text_filename = "An Introduction to Linear Regression Analysis.txt"
    text_file = text_path + text_filename
    text_obj = Text_Object(text_file)
    
    text_obj.extract_features()
    
    text_obj.pre_process()
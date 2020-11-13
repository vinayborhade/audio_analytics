# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:24:50 2020

@author: Vinay Borhade
"""
import pandas as pd

class Text_Object(object):
    def __init__(self, text_file):
        self.text_df = pd.read_excel(text_file)
        self.models = []
        
    def extract_features(self):
        print('In Text_Object.extract_features')
    
    def pre_process(self):
        print('In Text_Object.pre_process')

    # def register_models(self, model):
    #     self.models.append(model)
        
        
if __name__ == "__main__":
    text_path = "./text/"
    text_filename = "An Introduction to Linear Regression Analysis.xlsx"
    text_file = text_path + text_filename
    text_obj = Text_Object(text_file)
    
    print(text_obj.text_df)
    
    text_obj.extract_features()
    
    text_obj.pre_process()
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:24:50 2020

@author: Vinay Borhade
"""

class Text_Classifier_Model(object):
    
    def __init__(self):
        self.model = None
        self.data = None
        
    def set_model(self, model):
        self.model = None
        
    def set_data(self, data):
        self.data = data
        
    def train_model(self):
        print('In Text_Classifier_Model.train_model')
    
    def test_model(self):
        print('In Text_Classifier_Model.test_model')
        
if __name__ == "__main__":
    
    model = Text_Classifier_Model()  
    
    data = None
    model.set_data(data)
    
    model.train_model()
    
    model.test_model()
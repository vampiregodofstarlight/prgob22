# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 00:16:51 2022

@author: david
"""

class TV:
    def __init__(self, tv_name, current_volume, current_channel, max_volume, max_channel):
        self.tv_name=tv_name
        self.current_volume=current_volume
        self.max_volume=max_volume
        self.current_channel=current_channel
        self.max_channel=max_channel
        
    def change_channel(self, new_channel):
        if 0<=new_channel<=self.max_channel:
            self.current_channel = new_channel
            return True
        else:
            return False
        
    def increase_volume(self):
        if 0<=self.current_volume+1<=self.max_volume:
            self.current_volume+=1
            return True
        else:
            return False
    
    def decrease_volume(self):
        if 0<=self.current_volume-1<=self.max_volume:
            self.current_volume-=1
            return True
        else:
            return False
        
    def __str__(self):
        return f'{self.tv_name}, channel: {self.current_channel}, volume: {self.current_volume}'
    
    def str_for_file(self):
        return f'{self.tv_name},{self.current_volume},{self.current_channel},{self.max_volume},{self.max_channel}'
    
    
    
tv = TV('Living room TV', 2,22,7,9)
tv2 = TV('Bed room TV', 50,7,20,4)

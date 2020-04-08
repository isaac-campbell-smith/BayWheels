import numpy as np
import pandas as pd
import pickle
import collections
import os

class BikeData():
    def __init__(self, files):
        self.files = files
        
    def do_on_all(self, func):  
        data_dict = collections.OrderedDict()
        for file in self.files:
            pickle_in = open(file, 'rb')
            current_df = pickle.load(pickle_in)
            #v = func(current_df)
            return func(current_df)
            
            if v:
                data_dict[file[7:13]] = v
                pickle_in.close()
                return data_dict
            else:
                pickle_in.close()

    def collect_on_all(self, func):
        data_collect = np.array([])
        for file in self.files:
            pickle_in = open(file, 'rb')
            current_df = pickle.load(pickle_in)
            values = func(current_df)
            if data_collect.size == 0:
                data_collect = values
            else:
                data_collect += values
            pickle_in.close()
        return data_collect


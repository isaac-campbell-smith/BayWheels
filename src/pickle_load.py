import numpy as np
import pandas as pd
import pickle
import collections
import os
months = {'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', '06':'Jun',
          '07':'Jul', '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}
class BikeData():
    def __init__(self, files):
        self.files = files
        
    def do_on_all(self, func):  
        data_dict = collections.OrderedDict()
        for file in self.files:
            name = "{0} '{1}".format(months[file[11:13]], file[9:11])
            pickle_in = open(file, 'rb')
            current_df = pickle.load(pickle_in)
            value = func(current_df)
            data_dict[name] = value
            pickle_in.close()
        return data_dict
            #else:
                #pickle_in.close()

    def collect_on_all(self, func):
        data_collect = np.array([])
        for file in self.files:
            pickle_in = open(file, 'rb')
            current_df = pickle.load(pickle_in)
            values = func(current_df)
            data_collect = np.append(data_collect, values)
            pickle_in.close()
        return data_collect

    def sum_on_all(self, func):
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

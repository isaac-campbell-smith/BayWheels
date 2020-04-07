import numpy as np
import pandas as pd
import pickle
import os

### Read all the monthly reports into one dataframe


class BikeData():
    def __init__(self, files):
        self.files = files
        
    def do_on_all(self, func):  
        for file in self.files:
            pickle_in = open(file, 'rb')
            current_df = pickle.load(pickle_in)
            func(current_df, file)
            pickle_in.close()
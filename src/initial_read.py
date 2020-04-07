import numpy as np
import pandas as pd
import pickle
import os

### Read all the monthly reports into dataframes & pickle
def read_and_pickle(): 
    folder = 'gal/BayWheels/data/'
    files = sorted([folder+file for file in os.listdir(folder) 
                    if not (file.startswith('.') or file.startswith('2017'))]) #the 2017 data contains 6 months so won't parse for now

    for f in files:
        current_df = pd.read_csv(f)
        pickle_out = open("{}.pickle".format(f[:-23]), 'wb')
        pickle.dump(current_df, pickle_out)
        pickle_out.close()
        
read_and_pickle()

import numpy as np
import pandas as pd
import pickle
import os
### This script is for use in the terminal to speed up future calculations on the new pickled objects
### Read all the monthly reports into dataframes, perform some heavy functions & pickle
def read_and_pickle(): 
    folder = 'gal/BayWheels/data/'
    files = sorted([folder+file for file in os.listdir(folder) 
                    if not (file.startswith('.') or file.startswith('2017'))]) #the 2017 data contains 6 months so won't parse for now
    for f in files:
        current_df = pd.read_csv(f)
        current_df = current_df[['duration_sec', 'start_time', 'end_time', 'start_station_latitude', 
                                 'start_station_longitude', 'end_station_latitude', 'end_station_longitude',
                                 'bike_id', 'user_type']]
        revised_df = update_df(current_df)
        pickle_out = open("{}.pickle".format(f[:-23]), 'wb')
        pickle.dump(revised_df, pickle_out)
        pickle_out.close()

def update_df(df):
    day_dict = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}

    time = df.start_time
    dates = (time.apply(lambda date: date.split('-')[2][:2])).rename('date') #the original string is formatted y-m-d t:i:m:e

    time = time.apply(lambda date: pd.to_datetime(date))    
    weekends = (time.apply(lambda date: date.weekday() in [5,6])).rename('weekend') #dt.weekday returns a list value, 5 & 6 are Sat & Sun    
    day_of_week = (time.apply(lambda date: day_dict[date.weekday()])).rename('day_of_week')
    
    distance = distance_calculations(df)
    new_df = pd.concat([dates, day_of_week, weekends, df.bike_id, df.user_type, df.duration_sec, distance], axis=1)
    return new_df

def distance_calculations(df=None,file=None):
    from geopy import distance as dis
    from geopy import Point

    start_lat, start_long = df.start_station_latitude, df.start_station_longitude
    end_lat, end_long = df.end_station_latitude, df.end_station_longitude

    start_locs = (start_lat.astype('str') + ' ' 
                + start_long.astype('str')).apply(lambda x: Point(x))

    end_locs = (end_lat.astype('str') + ' ' 
                + end_long.astype('str')).apply(lambda x: Point(x))
    #what's this do
    dist_travelled = (pd.concat([start_locs, end_locs], axis=1)
                  .apply(lambda locs: dis.distance(locs[0], locs[1]).miles, axis=1)).rename('distance')
    
    dist_travelled = pd.concat([start_lat, start_long, end_lat, end_long, dist_travelled], axis=1)
    return dist_travelled
read_and_pickle()

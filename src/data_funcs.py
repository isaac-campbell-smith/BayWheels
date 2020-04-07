import numpy as np
import pandas as pd
import datetime
target_columns = ['start_time', 'end_time', 'start_station_latitude', 
                    'start_station_longitude', 'end_station_latitude', 'end_station_longitude']
def check_problem_columns(df=None, file=None, columns_that_cant_be_null=target_columns):        
    problem_columns = []
    for col in columns_that_cant_be_null:
        problem_rows = df[df[col].isna()]
        if problem_rows.size > 0:
                problem_columns.append(col)
        if len(problem_columns) > 0:
            print (file)
            print (problem_columns)
    return

def rentals_per_month(df=None, file=None):
    rentals = df['start_time'].size
    print ("{0}  :  {1}".format(file[7:13], rentals))
    return    

def weekend_averages(df=None, file=None):
    time = df['start_time']
    
    dates = (time.apply(lambda date: date.split('-')[2][:2])).rename('dates') #the original string is formatted y-m-d t:i:m:e
        
    time = time.apply(lambda date: pd.to_datetime(date))    
    weekends = (time.apply(lambda date: date.weekday() in [5,6])).rename('weekends') #dt.weekday returns a list value, 5 & 6 are Sat & Sun    
    day_of_week = (time.apply(lambda date: date.weekday())).rename('day_of_week')
    
    new_df = pd.concat([dates, day_of_week, weekends], axis=1)

    wk_group = new_df.groupby('weekends')['dates']
    number_of_days = int(max(dates)) #returns 28, 30 or 31 depending on length of month
    number_of_weekends = wk_group.nunique()[True] #counts the number of unique days where the weekend col is True
    number_of_weekdays = number_of_days - number_of_weekends

    weekend_ratio = number_of_weekends/number_of_days
    weekday_ratio = number_of_weekdays/number_of_days
        
    total_trips = dates.size
        
    expected_weekend_trips = int(total_trips*weekend_ratio)
    expected_weekday_trips = int(total_trips*weekday_ratio)
        
    actual_weekend_trips = wk_group.size()[True]
    actual_weekday_trips = wk_group.size()[False]

    biggest_date = dates.value_counts().idxmax()
    smallest_date = dates.value_counts().idxmin()
    biggest_day = new_df[new_df['dates'] == biggest_date].day_of_week.min()
    smallest_day = new_df[new_df['dates'] == smallest_date].day_of_week.min()
    print (file[7:13])
    print ("Total Weekend Trips: {0} | expected:  {1}".format(actual_weekend_trips, expected_weekend_trips))     
    print ("Total Weekday Trips: {0} | expected:  {1}".format(actual_weekday_trips, expected_weekday_trips))
    print ("Most popular day was on: {0} | Least popular day was on: {1}".format(biggest_day, smallest_day))

def distance_calculations(df=None,file=None):
    from geopy import distance as dis
    from geopy import Point
    start_locs = (df.start_station_latitude.astype('str') + ' '
                  + df.start_station_longitude.astype('str')).apply(lambda x: Point(x))
    end_locs = (df.end_station_latitude.astype('str') + ' ' 
                + df.end_station_longitude.astype('str')).apply(lambda x: Point(x))
    dist_travelled = (pd.concat([start_locs, end_locs], axis=1)
                  .apply(lambda locs: dis.distance(locs[0], locs[1]).miles, axis=1))
    avg_trip = dist_travelled.mean()
    times_where_less = (dist_travelled < .1).sum()
    print (file[7:13])
    print ("Average Trip: {:2.2f} miles".format(avg_trip))
    print ("# of Short Trips: {}".format(times_where_less))
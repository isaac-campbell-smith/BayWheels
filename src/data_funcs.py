import numpy as np
import pandas as pd
import datetime

def rentals_per_month(df=None):
    rentals = df['start_time'].size
    #print ("{0}  :  {1}".format(file[7:13], rentals))
    return rentals

def bikes_per_month(df=None):
    bikes = df.bike_id.nunique()
    return bikes

def subscribers_per_month(df=None):
    sub_rents = df[df.user_type == 'Subscriber'].date.size
    sub_rents /= df.date.size
    return sub_rents
    print ("{0} : {1:2.2f}".format(file[7:13], sub_rents))

def weekend_insights(df=None, file=None):
    wk_group = df.groupby('weekend')['date']
    number_of_days = int(max(df.date)) #returns 28, 30 or 31 depending on length of month
    number_of_weekends = wk_group.nunique()[True] #counts the number of unique days where the weekend col is True

    total_trips = df.date.size
    weekend_ratio = number_of_weekends/number_of_days 
    expected_weekend_trips = int(total_trips*weekend_ratio)
        
    actual_weekend_trips = wk_group.size()[True]

    biggest_date = df.date.value_counts().idxmax()
    smallest_date = df.date.value_counts().idxmin()
    biggest_day = df[df.date == biggest_date].day_of_week.min()
    smallest_day = df[df.date == smallest_date].day_of_week.min()
    print (file[7:13])
    print ("Total Weekend Trips: {0} | expected:  {1}".format(actual_weekend_trips, expected_weekend_trips))  
    print ("Most popular day was on: {0} | Least popular day was on: {1}".format(biggest_day, smallest_day))
    return

def weekly_popularity(df=None):
    wk_group = df.groupby('day_of_week')
    return (df.day_of_week.value_counts())
    #return 

def distance_insights(df=None):
    avg_trip = df.distance.mean()
    times_where_less = (df.distance < .1).sum()
    #print (file[7:13])
    print ("Average Trip: {:2.2f} miles".format(avg_trip))
    print ("# of Short Trips: {}".format(times_where_less))
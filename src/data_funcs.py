import numpy as np
import pandas as pd
import datetime

def rentals_per_month(df=None):
    rentals = df.date.size
    #print ("{0}  :  {1}".format(file[7:13], rentals))
    return rentals#/int(max(df.date))

def bikes_per_month(df=None):
    bikes = df.bike_id.nunique()
    return 

def weekday_v_weekend_distances(df=None):
    miles1 = df[df.weekend == False].distance.mean()
    miles2 = df[df.weekend == True].distance.mean()
    return miles1, miles2

def weekday_v_weekend_times(df=None):
    time1 = df[df.weekend == False].duration_sec.mean()
    time2 = df[df.weekend == True].duration_sec.mean()
    return time1, time2

def subscribers_per_month(df=None):
    sub_rents = df[df.user_type == 'Customer'].date.size
    #sub_rents /= df.date.size
    return sub_rents
    print ("{0} : {1:2.2f}".format(file[7:13], sub_rents))

def weekend_insights(df=None):
    wk_group = df.groupby('weekend')['date']
    number_of_days = int(max(df.date)) #returns 28, 30 or 31 depending on length of month
    number_of_weekends = wk_group.nunique()[True] #counts the number of unique days where the weekend col is True

    total_trips = df.date.size
    weekend_ratio = number_of_weekends/number_of_days 

    actual_weekend_trips = wk_group.size()[True]

    expected_weekend_trips = int(total_trips*weekend_ratio) - actual_weekend_trips

    #biggest_date = df.date.value_counts().idxmax()
    #smallest_date = df.date.value_counts().idxmin()
    #biggest_day = df[df.date == biggest_date].day_of_week.min()
    #smallest_day = df[df.date == smallest_date].day_of_week.min()
    #print ("Total Weekend Trips: {0} | expected:  {1}".format(actual_weekend_trips, expected_weekend_trips))  
    #print ("Most popular day was on: {0} | Least popular day was on: {1}".format(biggest_day, smallest_day))
    return actual_weekend_trips, expected_weekend_trips

def weekly_popularity(df=None):
    wk_group = df.groupby('day_of_week')
    order = []
    return (df.day_of_week.value_counts())
    #return 

def monthly_short_trips(df=None):
    df_slice = df[df.user_type == 'Customer']
    #avg_trip = df.distance.mean()
    times_where_less = ((df.distance < .1) & (df.start_station_latitude != 0)).sum()/df.date.size
    return times_where_less

def trip_activity(df=None):
    custs = df.user_type == 'Customer'
    cust_grp = df[custs]
    money_grp = df[custs & (df.duration_sec > 60*30)]
    #cust_grp2 = df[(df.user_type == 'Subscriber') & (df.duration_sec > 60*45)]
    return money_grp.date.size/cust_grp.date.size
    

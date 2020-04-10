import numpy as np
import pandas as pd
import pickle
from scipy import stats
month_grp = ['month', 'year']

day_lst = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']   
month_lst =[('Jan', '2018'),
            ('Feb', '2018'),
            ('Mar', '2018'),
            ('Apr', '2018'),
            ('May', '2018'),
            ('Jun', '2018'),
            ('Jul', '2018'),
            ('Aug', '2018'),
            ('Sep', '2018'),
            ('Oct', '2018'),
            ('Nov', '2018'),
            ('Dec', '2018'),
            ('Jan', '2019'),
            ('Mar', '2019'),
            ('Apr', '2019'),
            ('May', '2019'),
            ('Jun', '2019'),
            ('Jul', '2019'),
            ('Aug', '2019'),
            ('Sep', '2019'),
            ('Oct', '2019'),
            ('Dec', '2019'),
            ('Jan', '2020'),
            ('Feb', '2020')]

class BikeData():
    def __init__(self, file):
        pickle_in = open(file, 'rb')
        self.df = pickle.load(pickle_in)
        pickle_in.close()

    def rentals_per_month(self):
        grp = self.df.groupby(month_grp)
        return grp.size().reindex(month_lst)

    def revenue_per_month(self):
        grp = self.df.groupby(month_grp)
        return grp.revenue.sum().reindex(month_lst)

    def weekly_popularity(self):
        wk_group = self.df.groupby('day_of_week')
        return wk_group.size().reindex(day_lst)

    def monthly_short_trips(self):
        short_grp = self.df[(self.df.distance < .1) & 
                            (self.df.start_station_latitude != 0)]
        short_grp = short_grp.groupby(month_grp)
        whole_grp = self.df.groupby(month_grp)
        ratio = short_grp.size() / whole_grp.size()
        return ratio.reindex(month_lst)

    def proportion_of_customers(self): ##DOOOOOO ITTTTTTT
        cust_grp = self.df[self.df.user_type == 'Customer'].groupby(month_grp)
        whole_grp = self.df.groupby(month_grp)
        ratio = cust_grp.size() / whole_grp.size()
        return ratio.reindex(month_lst) 
        
    def weekday_v_weekend_distances(self):
        wkday = self.df[self.df.weekend == False].distance.mean()
        wkend = self.df[self.df.weekend == True].distance.mean()
        return wkday, wkend

    def weekday_v_weekend_times(self):
        wkday = self.df[self.df.weekend == False].duration_sec.mean()
        wkend = self.df[self.df.weekend == True].duration_sec.mean()
        return wkday, wkend

    def weekday_v_weekend_profits(self):
        wkday = self.df[self.df.weekend == False].revenue.mean() / 60
        wkend = self.df[self.df.weekend == True].revenue.mean() / 60
        return wkday, wkend

    def weekday_v_weekend_customers(self):
        custs = (self.df[self.df.user_type == 'Customer']
                     .groupby('weekend').user_type.value_counts())
        all_trips = self.df.groupby('weekend').user_type.size()

        wkday = custs[0] / all_trips[0]
        wkend = custs[1] / all_trips[1]
        return float(wkday), float(wkend)
    
    def big_money_probability(self):
        bool_mask = (self.df.month == 'Dec') & (self.df.year == '2019')
        idx = bool_mask.to_numpy().nonzero()[0][0]

        before_grp = self.df.iloc[:idx]
        before_grp = before_grp[before_grp.user_type == 'Customer']
        after_grp = self.df.iloc[idx:]
        after_grp = after_grp[after_grp.user_type == 'Customer']

        before_prob = (before_grp[before_grp.revenue > 2]
                        .user_type.size / before_grp.user_type.size)
        after_prob = (after_grp[after_grp.revenue > 2]
                        .user_type.size / after_grp.user_type.size)

        before_std = np.sqrt(before_prob*(1-before_prob))
        after_std = np.sqrt(after_prob*(1-after_prob))
        return [[before_prob, before_std], [after_prob, after_std]]
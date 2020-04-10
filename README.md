<p align="justify">
As a life-long resident of Tacoma (or Seattle for those reading this abroad), I struggle to look outside the Washington way of doing things. When Bike & Scooter sharing apps started popping up a few years ago, I'd hear story after story of people throwing them into the water and see, in my opinion, entirely too many drunken joy rides on a weekend night. When I heard that the San Francisco's BayWheels publishes all their monthly trip data, I was inspired to prove this new trend is a hedonistic stain on society.
    
At first glance, this BayWheels business seems to be pretty popular with almost 6,500 trips per day! If I'm right, then this will only magnify the power of my strongly worded disapproval.
 
<p align="center">    
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/Growth.png" />

<p align="justify">
It turns out that I was wrong. This actually became apparent pretty quickly. And I will admit that they seem to satisfy a pretty cool market niche for weekday commutes.
<p align="justify">
If I had been right, some of the observations you might expect to observe is an uptick in weekend rides and a large proportion of trips clocked at 0 zero miles. The reality is that BayWheels is much more popular on weekdays during normal commuting hours where the typical ride is about 1 mile. San Franciscans take about 7,300 trips per week day vs 4,100 trips per weekend day. The data also says that less than 4% of trips each month are less than 1/10th of a mile and users bike around at about 0.15 miles per minute.  </p>


<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/TripsperDay.png" />
<p></p>
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/TripTimeDistribution.png"/>
<p></p>
<div>
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/ShortTripsProportion.png" width="450" align='left'/>

<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/TimevDistance.png" width="450" align='right'/>
</div>
<div>
<p align="justify">
There is one huge caveat to all these findings, which is the influence of tourism - who knows if any of these trips are by work commuters! All trip logs are anonymous so it's pretty difficult to sus out any definitive answers, but BayWheels does include whether a trip was made by a 'Subscriber' (those with a special transit card or a monthly/yearly membership) or a 'Customer' (one time use). Up until December 2019, when they unleashed a swathe of new models across the Bay, a typical monthly proportion of 'Customer' trips hovered around 12-13%, with a few percentage points increase during summer months. </p> </div>  
    
<p align="center">    
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/CustomerProportion.png" width="520" align="center"/>
</p>    
<p align="justify">    
The fact that there was such a big spike in one-time trip purchases this last December seems to indicate that these are locals trying them out for the first time and it looks like they were retaining some percentage of these first-timers as new "Subscribers". It should be noted that a monthly membership is $15 for unlimited 45 minute rides, $2 for a 30 minute one time trip, or $10 for an unlimited 30 minute trip day pass (these trips are considered 'Customers' as well). The cost/benefit to a tourist visiting for more than a few days to spring for a membership is pretty powerful so this analysis may be completely wrong. 
    
<p align="justify">
This was my first experience working locally with a huge data set and my gosh was it a pain. The data was fairly clean which was a huge relief, but there were some column-wise calculations needing to be performed, which, over 5 million data points across 27 csv files, was not easy. Over the course of the week I became fairly comfortable with pickling data. For the unfamiliar, Pickle is a python module that serializes object data into a Wingdings font which apparently makes it super fast for the computer to return to that object's state (note: that's not entirely accurate). When I did my typical pd.readcsv and performed the desired calculations/transormations, it took about 45 minutes. My first thought was to just break up each csv and iterate through, but as I wrote more and more aggregate functions my code got to be pretty bonkers. Plus whenever I started a new kernel in Jupyter, the initial dataframe transformations took another 45 minutes. After much humming and hawing I did finally arrive at one giant transformed dataframe, which I then pickled, and it vastly improved my workflow. 

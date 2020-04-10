<p align="justify">
As a life-long resident of Tacoma (or Seattle for those reading this abroad), I struggle to look outside the Washington way of doing things. When Bike & Scooter sharing apps started popping up a few years ago, I'd hear story after story of people throwing them into the water. I'd see, in my opinion, entirely too many drunken joy rides on an otherwise peaceful Saturday night. When I heard that San Francisco's BayWheels publishes all their monthly trip data, I was inspired to prove this new trend a hedonistic stain on society.

At first glance, this BayWheels business seems to be pretty popular with almost 6,500 trips per day! If I'm right, then this will only magnify the power of my strongly worded disapproval.
 
<p align="center">    
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/Growth.png" />

<p align="justify">
It turns out that I was wrong. This actually became apparent pretty quickly. And I will admit that BayWheels seems to satisfy a pretty cool market niche for weekday commutes.
    
<p align="justify">
If I had been right, some of the observations you might expect to observe is an uptick in weekend rides and a large proportion of trips clocked at 0 zero miles. The reality is that BayWheels is much more popular on weekdays during normal commuting hours where the typical ride is about 1 mile. 
<p></p>
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/TripsperDay.png" />
<p></p>
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/TripTimeDistribution.png"/>
<p></p>
<p align="justify"> San Franciscans take about 7,300 trips per week day vs 4,100 trips per weekend day. The data also says that less than 4% of trips each month are less than 1/10th of a mile and users bike around at about 0.15 miles per minute.
<p></p>    
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/ShortTripsProportion.png"/>
<p></p>
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/TimevDistance.png"/>
<p></p>

<p align="justify">
There is one huge caveat to all these findings, which is the influence of tourism - who knows if any of these trips are actually by commuters! All trip logs are anonymous so it's pretty difficult to sus out any definitive answers, but BayWheels does include whether a trip was made by a 'Subscriber' (those with a special transit card or a monthly/yearly membership) or a 'Customer' (one time use). Up until December 2019, when they unleashed a swathe of new models across the Bay, a typical monthly proportion of 'Customer' trips hovered around 12-13%, with a few percentage points increase during summer months. </p> 
    
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/CustomerProportion.png"/>

<p align="justify">    
The fact that there was such a big spike in one-time trip purchases this last December seems to indicate that these are locals trying them out for the first time, and that BayWheels are likely retaining some percentage of these first-timers as new "Subscribers". It should be noted that a monthly membership is $15 for unlimited 45 minute rides, $2 for a 30 minute one time trip, or $10 for an unlimited 30 minute trip day pass (these trips are considered 'Customers' as well). All trips beyond these breakpoints incur a $3 per 15 minute chunk. The cost/benefit to a tourist visiting for more than a few days to just spring for a membership is pretty powerful, so this analysis may be completely innacurate. But the fact that trip durations cluster so strongly around 500 seconds (8 minutes) - a pretty quick trip - leads me to believe that this analysis is at least a little be right.
    
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/TripDurationDistribution.png"/>
<p></p>

<p align="justify">
Having already arrived at a wholly new understanding of this bike share phenomenom (in San Francisco anyway), I then grew curious about the general profitability of BayWheels and whether there were noticeable differences in weekend activity. I did learn that there are about 340 trips per month on average that get logged as over $50, about a third of these being over $150!
Customers are 10 times more likely to make this, what I assume to be, mistake. It's possible there is some promotion floating around every month for rides with an unlimited duration, but until I find proof (trust me I looked), I can only assume that the BayWheels customer service department has dealt with some pretty angry bike sharers.
    
<p align="justify">
At any rate, the data does show that typical weekend riders hold onto their bikes a bit longer - though not much further - and have a greater proportion of one-time "Customer"s. 
    
<p></p>
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/Week_v_end.png"/>
<p></p>    

<p align="justify">
With their recent spike in customer rates (and thus per trip revenue) I also wanted to see if they were primed for higher marginal profits, specifically, whether this new customer base is paying more money per trip (beyond the upfront $2). The data does not seem to say so and I'd imagine their revenue to trip ratio is settling back to a more typical level, in a parallel quarantine-free world anyway.
    
<p></p>
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/BigMoneyDistribution.png"/>
<p></p>
    
<p align="justify">
While I'm not entirely convinced Washington bike shares provide a net benefit, it was encouraging to learn something positive about eco-friendly transportation. This was my first experience working locally with a huge data set and my gosh was it a pain. The data was fairly clean which was a huge relief, but there were several column-wise calculations needing to be performed upfront, which, over 5 million data points across 27 csv files, was not easy. Over the course of the week I became fairly comfortable with pickling data. For the unfamiliar, Pickle is a python module that serializes object data into a Wingdings font, which apparently makes it super fast for the computer to return to that object's saved state (note: that's not entirely accurate). When I did my typical pd.readcsv and performed the desired calculations/transormations, it took about 45 minutes. My first thought was to just break up each csv and iterate through, but as I wrote more and more aggregate functions my code got to be pretty bonkers. Plus whenever I started a new Jupyter kernel, the initial dataframe transformations would take another 45 minutes. After much humming and hawing I finally arrived at one giant transformed dataframe, which I then pickled, and it vastly improved my workflow. If you are curious about working with this data I highly recommend checking out my initial_read script and modifying it to your liking. I left out some geographic information in my final DataFrame that is probably worth exploring. Due to my lack of domain knowledge of San Francisco, I ultimately decided it wasn't a good use of my limited time.

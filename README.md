<p align="justify">
As a life-long resident of Tacoma (or Seattle for those reading this abroad), I struggle to look outside the Washington way of doing things. When Bike & Scooter sharing apps started popping up a few years ago, I'd hear story after story of people throwing them into the water and see, in my opinion, entirely too many drunken joy rides on a weekend night. When I heard that the San Francisco's BayWheels publishes all their monthly trip data, I was thus inspired to prove this activity is a complete stain on society.
    
 At first glance, this bike share seems to be pretty popular!
    
<p align="justify">
    
Over the course of the next week I'll be looking at the trip data for this service and see what kind of things I can learn. My working hypothesis about this service, and my assumption about bike sharing services generally, is that most people are using them for the novelty and not commuting or other functional purposes. I am prepared to be wrong!

<p align="center">    
    <img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/Charts/Growth.png"/>

<p align="justify">
This was my first experience working locally with a huge data set and my gosh was it a pain. The data was fairly clean which was a huge relief, but there were some column-wise calculations needing to be performed, which, over 5 million data points across 27 csv files, was not easy. Over the course of the week I became fairly comfortable with pickling data. For the unfamiliar, Pickle is a python module that serializes object data into a Wingdings font which apparently makes it super fast for the computer to return to that object's state (note: that's not entirely accurate). When I did my typical pd.readcsv and performed the desired calculations/transormations, it took about 45 minutes. My first thought was to just break up each csv and iterate through, but as I wrote more and more aggregate functions my code got to be pretty bonkers. Plus whenever I started a new kernel in Jupyter, the initial dataframe transformations took another 45 minutes. After much humming and hawing I did finally arrive at one giant transformed dataframe, which I then pickled, and it vastly improved my workflow. 

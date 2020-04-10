<p align="justify">
Welcome to my exploratory data analysis of the last 2 years of Lyft's Bay Area CA bike sharing service, Bay Wheels! This repo was prepared during as first capstone project as a student at Galvanize Seattle. Shall we dive in?
<p align="justify">
This was my first experience working locally with a huge data set and my gosh was it a pain. The data was fairly clean which was a huge relief, but there were some column-wise calculations needing to be performed, which, over 5 million data points across 27 csv files, was not easy. My computer fan was the true hero throughout the week. Here's what the initial data looked like:
    
<p align="justify">
    
Over the course of the next week I'll be looking at the trip data for this service and see what kind of things I can learn. My working hypothesis about this service, and my assumption about bike sharing services generally, is that most people are using them for the novelty and not commuting or other functional purposes. I am prepared to be wrong!

<p align="center">    
    <img src="https://raw.githubusercontent.com/isaac-campbell-smith/BayWheels/master/charts/Growth.png" align="center"     alt="Company Growth" width="720" />



Overview of the data and their growth:
....ADD.........Plot
alkjdfladj
Two important but straightforward trends if my hypothesis holds, before getting into the weeds, would be:
    > More trips on the weekend (for leisure activites like doing wheelies on a novelty bike)
    > A large share of trips being short (let's say less than .1 miles)
    
Turns out I was wrong! Literally every month since January 2018 showed a proportionately lower level of bike trips on the weekends. The least popular day for BayWheels falls on a Sunday more than any other day. Saturdays aren't much better and Tues-Thurs seem to do very well.
.....ADD.....BAR GRAPH MONTHLY WEEKEND RIDES (SHADE EXPECTED)
.............HISTOGRAM OF LEAST POPULAR DAYS & MOST POPULAR DAYS

We can also see that average monthly trip distance is actually trending up and short trips make up less than 5% of the monthly rides
.....ADD.......average trip distance
.....ADD.......percentage of short trips

Without having gotten granular or performed any A/B tests with this data it's safe to say that people are probably using this bike service to commute around. It's true that tourism may be a big factor in this trip data but The weekday/weekend dropoff, even though it killed my initial hypothesis, is not significant enough to draw further conclusions about the original leisure hypothesis. It makes me wonder if it's popular with those in the service industry. So it seems prudent to segment out subscribers and casual customers and go from there.
.......ADD......Percentage

IS THEIR NEW BIKE FLEET AND SURGE IN POPULARITY LINKED TO THE SIZE OF THE FLEET?
There will be a lot of activity for subscribers will be somewhere around SanFran's nightlife and closer to there on the weekends. 
....source percentage of subscribers
.....Subscriber distances 
.....

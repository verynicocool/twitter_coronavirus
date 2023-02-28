# Coronavirus twitter analysis
This project uses the MapReduce model in order to quantify the amount of all geotagged twitter tweets sent in 2020 in terms of language and country.

Using matplotlib, I was able to create bar graphs that plot the top 10 of a certain paramater (country or language) whose tweets contain the either one of the tags (#coronavirus or #코로나바이러스). These plots are shown below:

## #coronavirus tweets

<img src=./graphs/reduced.country%23coronavirus.png width=100%/>
<img src=./graphs/reduced.lang%23coronavirus.png width=100%/>

We can see that #coronavirus was most used in the U.S. and the hashtag was most used in tweets language tagged as English

## #코로나바이러스 tweets

matplotlib was unable to display korean text and thus, the axes titles on the following plots display as squares rather than with #코로나바이러스 

<img src=./graphs/reduced.country%23코로나바이러스.png width=100%/>
<img src=./graphs/reduced.lang%23코로나바이러스.png width=100%/> 

We can see that #코로나바이러스 was most used in Korea and the hastag was most used in tweets language tagged as Korean


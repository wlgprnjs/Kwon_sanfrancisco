# San Francisco.
Data Mining course project based on the data sets from https://data.sfgov.org/ 

Thought Process: 
Find out which type of crashes are frequent for intersection and midblock
Create separate cluster graphs for weekday and weekend
With Clustering find those center of those clusters for weekend and weekday
Which roads to be cautious on
What type of accident to keep an eye out for (pro-active driving) 

Initally wanted to create a day of the week, if there is a correlation between the day of the week and the type of collisions.
For example, mondays have more sideswipe ( maybe from first day of work of the week), Saturdays have more head-to-head collision from DUIs. 

 ** note to self, try to have a focus on a proposal **
	
** Pre-processing**
According to Google, rush hour in San Francisco is from 7:00 AM to 9:00 AM for morning commute and the evening commute from 4:00 PM to 6:00 PM
If rush hour  = 1; if not rush hour = 0
From Mon-Fri are labeled as weekdays, Sat - Sun are labeled as weekends
Severity num represents collision severity
Injury (Other Visible) =1
Injury (Complaint of Pain)= 2
Injury (Severe)= 3

Column Name ---> Description
unique_id - unique table row identifier
tb_latitude - Latitude of Crash
tb_longitude - Longitude of Crash
collision_time - The time when the crash occurred (24 hour time)
month - Month crash occurred
day_of_week - Day of the week crash occurred
collision_severity - Injury level severity of the crash
type_of_collision - Type of crash
intersection - Indicates whether the crash occurred in an intersection
weather_1 - The weather condition at the time of crash

**Machine model:**
  Identifies accident prone areas based on location patterns from the database weekdayClusters and WeekendClusters. It takes the longitude and latitude for clustering and then K-means is applied. For weekdays 7 clusters are assigned while for weekends 4 clusters. The number of clusters are not the same because the weekday had significant more data. 

**Visualizaion:**
  For clustering map, Seaborn and Matplotlib were used. The red strats indicated cluster cenrtoids. This helped visualize hotspots and compare patterns between weekdays and weekends. 
  Tableau was also used to create visualization tables. A  for the number of different type of collision for intersection vs Midblock. This was shown with a Bar chart. Another visualization was created for the number of different type of collision for weekends and weekdays. This is shown with a treemap
  
**Conclusion:**
  From the model we can see that on weekdays, the seven areas to avoid/ to be cautious in. Fulton st. AND
Park Presidio Blvd, Market st, 19th st ANd Mission st, Park Presidio Blvd, 19th Ave AND Sloat Blvd, Revere ae
AND Silver Ave on week days. On weekends Golden Gate Ave AND S VanNess Ave, Martin Luther King Jr AND 19th Ave, Friday Kahlo Way AND Ocean Ave, Cortland Ave AND Bayshore Blvd shoud be avoided or have caution area those areas. With the visualizations and the datasets, we can see that the most frequent type of collision on weekday and weekends are Braodside and Vehicle to Pedestrian. For intersections, broadside ( two cars colliding in a 90 degree angle) and for midblock, sideswipe is the most common. 

Civilians of San Fransisco should be driving with a proactive mindset when it comes to the listed areas from the cluster map. They should be practicing pro-active driving when it comes intersections and midblocks, Keeping sideswipe and broadside in mind.

**After thoughts: **
I could have done a better job at merging the preprocessing files from one coding file. There were other data attributes I should have worked with but wasn't sure how it would relate, next time would be a good idea to attempt a model to test if there are any relations. 

Possibily utilize the days of the week as each day instead of weekday / weekends. 

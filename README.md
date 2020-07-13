# SQLAlchemy-Challenge
It’s time for a vacation! I have planned a trip to Honolulu, Hawaii. To help plan my trip, I am going to conduct some climate analysis in the area. Once I complete my data exploration and analysis, I will design a Flask API based on the results of my analysis. I will be exploring an [SQLite climate database](https://github.com/AlexandraOricchio/SQLAlchemy-Challenge/blob/master/Resources/hawaii.sqlite) using Python and SQLAlchemy. I will then conduct my analysis utilizing SQLAlchemy ORM queries, Pandas, and Matplotlib. 

## Climate Analysis and Exploration: 
Used SQLAlchemy to connect to the SQLite database. Explored precipitation data and analyzed last 12 months of data. Created a plot to visualize the precipitation values over the 12-month period and retrieved a statistics summary of the data using Pandas. 
![precipitation](Images/precipitation_analysis.JPG)
Explored station data and designed a query to find the most active stations. Created a histogram plot for the station with the highest number of temperature observations.

![station](Images/station_analysis.JPG)

## Climate Application:
Designed a Flask API based on my analysis and exploration of the data. Created a home page with a list of routes available.

![routes](Images/routes.JPG)

1. **Precipitation:** Converted my query results into a dictionary and returned the JSON representation of said dictionary.
![route1](Images/route1.JPG)

2. **Stations:** Returned a JSON list of all stations within the dataset.
![route2](Images/route2.JPG)

3. **Temperature Observations (tobs):** Queried dates and temperature observations for a year from the last data point and returned a JSON list of resulting data. 
![route3](Images/route3.JPG)

4. **Start date:** Based on the input start date, returned JSON list of minimum, maximum, and average temperature for all dates greater than or equal to start date. 
![route4](Images/route4.JPG)

5. **Start and End dates:** Based on the input for start and end date, returned JSON list of minimum, maximum, and average temperature for time period. 
![route5](Images/route5.JPG)

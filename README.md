# SQLAlchemy Homework - Surfs Up!

### Before You Begin

![surfs-up.png](Images/surfs-up.png)

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. T

## Step 1 - Climate Analysis and Exploration

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

### Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data.

* Plot the results.

  ![precipitation](Images/precipitation.png)

* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Design a query to calculate the total number of stations.

* Design a query to find the most active stations.

* Design a query to retrieve the last 12 months of temperature observation data (tobs).

  * Plot the results as a histogram with `bins=12`.

    ![station-histogram](Images/station-histogram.png)

- - -

## Step 2 - Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use FLASK to create your routes.

### Routes

* `/`: Home page. List all routes that are available.

* `/api/v1.0/precipitation`: Return the JSON representation of your dictionary.

* `/api/v1.0/stations`: Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`: Return a JSON list of Temperature Observations (tobs) for the previous year (from the last data point)

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

- - -

### Optional: Other Recommended Analyses

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

### Temperature Analysis II

* Plot the min, avg, and max temperature from your previous query as a bar chart.

  * Use the average temperature as the bar height.

  * Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr).

    ![temperature](Images/temperature.png)

### Daily Rainfall Average

* Calculate the rainfall per weather station using the previous year's matching dates.

* Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.

  ![daily-normals](Images/daily-normals.png)

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.

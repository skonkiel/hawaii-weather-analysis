# Hawai'i Weather Analysis

## Project background
This project analyzes historical weather station observations for Hawai'i and repurposes the data into a Flask-powered API. It answers questions like: 
* What are general trends in the last 12 months worth of preciptation and temperature data?
* How many stations collected weather observations, and which were the most active stations?
* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperatures in June and December?
* How much rain should you expect to encounter on any given day?

## Technologies used
* sqlite, to store the analyzed data
* SQLAlchemy, to load the analyzed data 
* Pandas, to analyze the data
* Matplotlib, to visualize the data
* Flask, to make the data available via API

## Installation

1. Clone this repository
2. Launch a Jupyter Notebook from Git Bash/Terminal (by running `jupyter notebook`). You will likely need to install some packages like SQLAlchemy, pandas, and Matplotlib. 
3. Open and run the `climate_starter.ipynb` Jupyter notebook to load and analyze the data.
4. Start a Flask server to work with the API endpoints. To start the server, first activate a Python virtual enviornment that has the necessary packages installed. From within the same folder as `app.py`, run `python app.py` from your Git Bash/Terminal window. You can then copy and paste the Flask URL into your browser to start working with the API and its various routes.

### Routes

* `/`: Home page. Lists all routes that are available.

* `/api/v1.0/precipitation`: Returns the JSON representation of your dictionary.

* `/api/v1.0/stations`: Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`: Returns a JSON list of Temperature Observations (tobs) for the previous year (from the last data point)

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

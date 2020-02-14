import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

# Database / ORM setup

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Flask setup

app = Flask(__name__)

# Route setup

@app.route('/')
def home():
    return (
        f"Welcome to the Hawai'i weather API.<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation - Precipitation figures<br/>"
        f"/api/v1.0/stations - Measurement stations<br/>"
        f"/api/v1.0/tobs - Temperature observations (F)<br/>"
        f"/api/v1.0/*start* - Minimum, Average, and Max temps for a date range starting on *start*<br/>"
        f"/api/v1.0/*start*/*end* - Minimum, Average, and Max temps for a date range starting on *start* & ending on *end*<br/>"
        f"Note: Dates should be formatted YYY-MM-DD"
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    
    '''get all precipitation data + dates for 8/23/2016 - 8/23/2017'''
    results = session.query(Measurement.date, Measurement.prcp) \
            .filter(Measurement.date <= '2017-08-23') \
            .filter(Measurement.date >= '2016-08-23').all()
    
    session.close()
    
    all_prcp = []
    
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict[date] = prcp
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)

@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    
    '''return a list of all stations in the dataset'''
    station_list = session.query(Station.station).all()
    
    session.close()
 
    d = []
    
    for x, in station_list:
        d.append(x)
        
    return jsonify(d)

@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    
    '''query for the dates and temperature observations from a year from the last data point'''
    temps = session.query(Measurement.date, Measurement.tobs) \
            .filter(Measurement.date <= '2017-08-23') \
            .filter(Measurement.date >= '2016-08-23').all()
    
    session.close()
    
    d = []
    
    '''Return a JSON list of Temperature Observations (tobs) for the previous year.'''
    for date, tobs in temps:
        t = []
        t.append(date)
        t.append(tobs)
        d.append(t)      
        
    return jsonify(d)


#  `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

@app.route('/api/v1.0/<start_date>')
def date(start_date):
    
    session = Session(engine)

    #   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
    temps = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)) \
            .filter(Measurement.date >= start_date).group_by(Measurement.date).all()

    session.close()

    d = {}

    for date, min_tobs, avg_tobs, max_tobs in temps:
        tobs = {}
        tobs['TMIN'] = min_tobs
        tobs['TAVG'] = avg_tobs
        tobs['TMAX'] = max_tobs
        d[date] = tobs
        
    return jsonify(d)

@app.route('/api/v1.0/<start_date>/<end_date>')
def two_date(start_date, end_date):
    
    session = Session(engine)
    
    '''When given the start and the end date, calculate the `TMIN`, `TAVG`, 
    and `TMAX` for dates between the start and end date inclusive.'''

    temps = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)) \
            .filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).group_by(Measurement.date).all()

    session.close()

    d = {}

    for date, min_tobs, avg_tobs, max_tobs in temps:
        tobs = {}
        tobs['TMIN'] = min_tobs
        tobs['TAVG'] = avg_tobs
        tobs['TMAX'] = max_tobs
        d[date] = tobs
        
    return jsonify(d)
    

if __name__ == "__main__":
    app.run(debug=True)













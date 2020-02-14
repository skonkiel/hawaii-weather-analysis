import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

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
        f"/api/v1.0/*start*/*end* - Minimum, Average, and Max temps for a date range starting on *start* & ending on *end*"
    )

if __name__ == "__main__":
    app.run(debug=True)













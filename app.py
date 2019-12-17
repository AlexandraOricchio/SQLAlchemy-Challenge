import numpy as np
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database setup
engine = create_engine(os.path.join("sqlite:///","Resources","hawaii.sqlite"))
# reflect 
Base = automap_base()
Base.prepare(engine, reflect=True)
# Save reference to the table
Measurement = Base.classes.measurement 
Station = Base.classes.station

# Flask setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():
     return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start/START_DATE<br/>"
        f"/api/v1.0/start/end/START_DATE/END_DATE"
    )

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    prcp = []
    for row in results:
        p_dict = {}
        p_dict["date"] = row[0]
        p_dict["prcp"] = row[1]
        prcp.append(p_dict)

    return jsonify(prcp)

# Stations Route
@app.route("/api/v1.0/stations")
def stations():
    session =  Session(engine)
    results = session.query(Station.name).all()
    session.close()

    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

# tobs Route
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results = session.query(Measurement.tobs).filter(Measurement.date <= '2017-08-23').filter(Measurement.date >= '2016-08-23').all()
    session.close()

    tobs_12_mos = list(np.ravel(results))
    return jsonify(tobs_12_mos)

# Start Date Route
@app.route("/api/v1.0/start/<start_date>")
def start(start_date):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start_date).all()
    session.close()

    return jsonify(results)

# Start and End Date Route
@app.route("/api/v1.0/start/end/<start_date>/<end_date>")
def start_end(start_date, end_date):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    session.close()

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
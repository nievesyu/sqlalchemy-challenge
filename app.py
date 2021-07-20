import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from sqlalchemy.sql.expression import true


#database setup
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)


# Measurement = Base.classes.measurement
Station = Base.classes.station



app = Flask(__name__)

@app.route("/")
def index():
    """List of all available routes."""
    return(
        f"Hello!!Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )



# @app.route("/api/v1.0/precipitation")
# def precipitation():
#     session = Session(engine)

if __name__ == '__main__':
    app.run(debug=true)

import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from sqlalchemy.sql.expression import true


#database setup
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)


# Measurement = Base.classes.measurement
Station = Base.classes.station



app = Flask(__name__)

@app.route("/")
def index():
    """List of all available routes."""
    return(
        f"Hello!!Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )



# @app.route("/api/v1.0/precipitation")
# def precipitation():
#     session = Session(engine)

if __name__ == '__main__':
    app.run(debug=true)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
	#name of the table inside our db
	__tablename__= "flights"
	#nullable = null not able
	id = db.Column(db.Integer, primary_key = True)
	origin = db.Column(db.String,nullable = False)
	destination = db.Column(db.String, nullable = False)
	duration = db.Column(db.Integer,nullable = False)

class Passenger (db.Model):
	__tablename__ = "passengers"
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String, nullable = False)
	#ForeignKey = some column that is referencing another table in our db
	flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"),nullable = False)

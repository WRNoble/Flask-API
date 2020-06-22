from flask import Flask, request, jsonify
import datetime, json
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('movies', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

class Movie(BaseModel):
    title = CharField(max_length=255, unique = True)
    vote_average = DecimalField()
    overview = CharField(max_length=500)
    release_date = DateTimeField()

db.connect()
db.create_tables([Movie])
  
app = Flask(__name__)

@app.route('/', methods=['GET'])
def endpoint1():
  movieList = []
  for movie in Movie.select():
      print(movie)
      movieList.append(model_to_dict(movie))
  return jsonify(movieList)
  # return "connected"

@app.route('/movie/<name>', methods=['GET'])
def endpoint2():
    if request.method == 'GET':
      if name:
        return jsonify(model_to_dict(Movie.get(Movie.name == name)))
      else:
        return "Sorry, the movie you requested could not be found."




app.run(port=5000, debug=True)
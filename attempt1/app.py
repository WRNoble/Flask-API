from flask import Flask, request, jsonify
import datetime
import json
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
db.drop_tables([Movie])
db.create_tables([Movie])

Movie(title='Rogue One', vote_average='9', overview='Rebels acquire plans to the Death Star', release_date='December 20, 2016').save()

with open('./data.json', 'r') as data:
  movies = json.load(data)
  
for movie in movies:
    Movie(
      title = movie['title'],
      vote_average = movie['vote_average'],
      overview = movie['overview'],
      release_date = movie['release_date']
    ).save()

jim = Movie.select()
print(jim)
app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def endpoint1():
#   movieList = []
#   for movie in Movie.select():
#       print(movie)
#       movieList.append(model_to_dict(movie))
#   return jsonify(movieList)

# @app.route('/movie/', methods=['GET', 'POST'])
# @app.route('/movie/<id>', methods=['GET'])
# def endpoint(id=None):
#   if request.method == 'GET':
#     if id:
#       return jsonify(model_to_dict(Movie.get(Movie.id == id)))
#     else:
#       movieList = []
#       for movie in Movie.select():
#         movieList.append(model_to_dict(movie))
#       return jsonify(movieList)

#     if request.method == 'POST':
#       new_movie = dict_to_model(Movie, request.get_json())
#       new_movie.save()
#       return jsonify({"success": True})

# app.run(port=5000, debug=True)

# jim = Movie.connect()
# print(jim)
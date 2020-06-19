from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('movies', user='postgres', password='', host='localhost', port=5432)


# MODELS
class BaseModel(Model):
  class Meta:
    database = db

class Movie(Model):
    name = CharField(max_length=255, unique = True)
    rating = IntegerField()
    director = CharField()
    date_released = DateField()
    cast = CharField()

db.connect()
db.drop_tables([Movie])
db.create_tables([Movie])


app = Flask(__name__)

# ROUTES

#   movies = []
#   return jsonify({'movies': movies})

# @app.route('/movie/', method=['GET', 'POST'])
# @app.route('/movie/<id>', methods=['GET', 'PUT', 'DELETE'])
# def endpoint(id=None):
#   if request.method == 'GET':
#     if id:
#         return jsonify(model_to_dict(Movie.id == id))
#     else:
#         movieList = []
#         for movie in Movie.select():
#             movieList.append(model_to_dict(movie))
#         return jsonify(movieList)

#     if request.method == 'PUT':
#         return 'PUT request'
    
#     if request.method == 'POST':
#         new_movie = dict_to_model(Movie, request.get_json())
#         new_movie.save()
#         return jsonify({"success": True})

#     if request.method == 'DELETE':
#         return 'DELETE request'

app.run(debug=True port=5000 )
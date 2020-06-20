from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('movies', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

class Movie(BaseModel):
    name = CharField(max_length=255, unique = True)
    rating = IntegerField()
    director = CharField()
    date_released = DateField()
    cast = CharField()

db.connect()
db.drop_tables([Movie])
db.create_tables([Movie])

Movie(name='Rogue One', rating='9', director='Gareth Edwards', date_released='December 20, 2016', cast='sad girl and angry guy').save()
Movie(name='Solo', rating='5', director='Ron Howard', date_released='May 10, 2018', cast='Emilia Clarke, Alden Ehrenreich, Donald Glover').save()
Movie(name='Holiday Special', rating='1', director='He who shall not be named', date_released='December 10, 1979', cast='sadness').save()

with open('./data.json') as moviesjson:
  movies = json.load(moviesjson)
  
for movie in movies:
    name = movie['name'],
    rating = movie['rating'],
    director = movie[director],
    date_released =movie['date_released']
    cast =movie['cast'].save()

app = Flask(__name__)

@app.route('/movie/', methods=['GET', 'POST'])
@app.route('/movie/<id>', methods=['GET'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
      return jsonify(model_to_dict(Movie.get(Movie.id == id)))
    else:
      movieList = []
      for movie in Movie.select():
        movieList.append(model_to_dict(movie))
      return jsonify(movieList)

    if request.method == 'POST':
      new_movie = dict_to_model(Movie, request.get_json())
      new_movie.save()
      return jsonify({"success": True})

app.run(port=5000, debug=True)
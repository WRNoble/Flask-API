from flask import Flask, jsonify, request, Blueprint
from .models import Movie

main = Blueprint('main',__name__)

@main.route('/', method=['GET'])
def all_movies():
  movies = []
  return jsonify({'movies': movies})

@main.route('/movie', method=['POST'])
def add_movie():
    movie_info = request.get_json()
    new = Movie(name = movie_info['name'], rating = movie_info['rating'], director = movie_info['director'], date_released = movie_info['date released'], cast = movie_info['cast'])
    db.session.add(new)
    db.session.commit()
    return 'Done', 201

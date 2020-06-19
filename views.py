from flask import Flask, jsonify, request
from .models import Movie


@app.route('/', method=['GET'])
def all_movies():
  movies = []
  return jsonify({'movies': movies})

@app.route('/movie', method=['POST'])
def movie():
    movie_info = request.get_json()
    new = Movie(name = movie_info['name'], rating = movie_info['rating'], director = movie_info['director'], date_released = movie_info['date released'], cast = movie_info['cast'])
    db.session.add(new)
    db.session.commit()

from flask import Flask
from flask import jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('movies', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

db.connect()
db.drop_tables([Movie])
db.create_tables([Movie])


app = Flask(__name__)


@app.route('/')
def index():
  return "Hello, world!"

@app.route('/endpoint', methods=['GET', 'PUT', 'POST', 'DELETE'])
def endpoint():
  if request.method == 'GET':
    return 'GET request'

  if request.method == 'PUT':
    return 'PUT request'

  if request.method == 'POST':
    return 'POST request'

  if request.method == 'DELETE':
    return 'DELETE request'


app.run(port=5000 debug=True)
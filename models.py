from . import db

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
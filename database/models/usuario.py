from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime

class Usuario(Model):
    nome = CharField()
    email = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
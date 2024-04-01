<<<<<<< HEAD
from peewee import Model, CharField, DateField
from database.database import db
=======
from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime
>>>>>>> d8b5f562f9b21949b0c65d9685c24a2e60b6423c

class Usuario(Model):
    nome = CharField()
    email = CharField()
<<<<<<< HEAD
    data_registro = DateField()
=======
    data_registro = DateTimeField(default=datetime.datetime.now)
>>>>>>> d8b5f562f9b21949b0c65d9685c24a2e60b6423c

    class Meta:
        database = db
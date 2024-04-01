<<<<<<< HEAD
from peewee import SqliteDatabase

db = SqliteDatabase('usermanager.db')
=======
from peewee import PostgresqlDatabase
import psycopg2

db = PostgresqlDatabase(database='usersmanager', user='postgres', host='localhost',
                        password='pgadmin')
>>>>>>> d8b5f562f9b21949b0c65d9685c24a2e60b6423c

from peewee import PostgresqlDatabase
import psycopg2

db = PostgresqlDatabase(database='usersmanager', user='postgres', host='localhost',
                        password='postgres')


# from peewee import SqliteDatabase

# db = SqliteDatabase('usermanager.db')


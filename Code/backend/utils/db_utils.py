import psycopg2
import os

def get_db_connection():
    """ Establishes a connection to the database """
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn

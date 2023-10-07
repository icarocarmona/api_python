import mysql.connector
from mysql.connector.pooling import MySQLConnection
import json
import uuid

# connection parameters
config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "db-78n9n",
    "database": "example",
}


class DAO(object):

    def __init__(self) -> None:
        self.cnx = mysql.connector.connect(**config)

    def insert(self, query, values):
        with self.cnx.cursor() as cursor:
            cursor.execute(query, values)
            lastrowid = cursor.lastrowid

            self.cnx.commit()
            return lastrowid

    def update(self, query, values):
        with self.cnx.cursor() as cursor:
            cursor.execute(query, values)
            rowcount = cursor.rowcount
            self.cnx.commit()
            return rowcount

    def select(self, query, values=()):
        with self.cnx.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchall()

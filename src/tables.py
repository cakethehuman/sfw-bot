import mysql.connector
from tabulate import tabulate
from time import sleep
import cachetools

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",#put your own pass:V
  database="user_data"
)

#mydb.commit() this is for update and other other shit
cache = cachetools.TTLCache(maxsize=100,ttl=5)
selection = "select * from interviews"

@cachetools.cached(cache)
def get_users(selection):

    mycursor = mydb.cursor()
    mycursor.execute(selection)
    interview_data = mycursor.fetchall()
    cache[selection] = interview_data
    return interview_data


interview_data = get_users(selection)

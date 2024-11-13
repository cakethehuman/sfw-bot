import mysql.connector
from tabulate import tabulate
from time import sleep
import cachetools


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",#put your own pass:V
  database="user_data"
)


#mydb.commit() this is for update and other other shit

cache = cachetools.TTLCache(maxsize=100, ttl=60)
@cachetools.cached(cache)
def get_data(selection):
  mycursor = mydb.cursor()
  mycursor.execute(selection)
  interview_data = mycursor.fetchall()
  return interview_data

get_data("select * from interviews") 
print(get_data("select * from interviews") )

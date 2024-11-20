import sqlite3
"""
so i would be building a way for people to do $apply and then there name will be added to the data base + give roles :V
"""

database = sqlite3.connect("user.db")
data = database.cursor()

#data.execute("""CREATE TABLE INTERVIEW(
                #Name varchar(255),
                #status bool
             #);""")
#data.execute("INSERT INTO INTERVIEW (name, status) VALUES ('cake', 0);")
def data_select():
    data.execute("select * from INTERVIEW")
    data_base_data = data.fetchall()
    print(data_base_data)
    return str(data_base_data)

def data_add():
    data.execute("INSERT INTO INTERVIEW (name,status) VALUES ('hello',1)")
    return "command run 100% cool cake likes"


data_select()
database.commit()

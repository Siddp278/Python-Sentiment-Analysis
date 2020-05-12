import sqlite3

con = sqlite3.connect('my_database.db')
curs = con.cursor()

curs.execute(""" create table reviews(title text, rating float(4,2), storyline text, genre text)""")

con.commit()
con.close()
import sqlite3
from docutils.nodes import row
conn=sqlite3.connect('music.sqlite')
cur=conn.cursor()
tup=("hello tuple",100)
cur.execute('INSERT INTO Tracks (plays, title) VALUES(?,?)',tup)
conn.commit()
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)
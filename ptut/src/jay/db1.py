import sqlite3
import matplotlib.pyplot as plt
conn=sqlite3.connect('tutorial.db')
c=conn.cursor()
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS mytable(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
def data_entry():
    c.execute('''INSERT INTO mytable VALUES(145256,
        '2016-01-01','python',5)''')
    c.execute('''INSERT INTO mytable(unix,datestamp,keyword, value)VALUES(?,?,?,?)''',
              (85466,'12-03-2019','python',25))
    conn.commit()
    c.close()
    conn.close()

def read_db():
    c.execute('SELECT * FROM mytable')
    for row in c.fetchall():
        print(row)
    conn.commit()
    c.close()
    conn.close()
def plot_db():
    c.execute('SELECT datestamp, value FROM mytable')
    d=[]
    v=[]
    for rows in c.fetchall():
        d.append(rows[0])
        v.append(rows[1])
    plt.plot(d,v)
    plt.show()
#create_table()
#data_entry()
#read_db()
plot_db()
    

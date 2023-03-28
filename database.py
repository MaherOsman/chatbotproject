'''
sql integration
'''

from database import connect_to_database

# Call the connect_to_database function to connect to your SQL database
connect_to_database()

'''
python
 import sqlite3

 # connect to database
 conn = sqlite3.connect('your-database.db')
 c = conn.cursor()

 # retrieve data from tables
 c.execute('SELECT * FROM courses')
 courses = c.fetchall()

 c.execute('SELECT * FROM prerequisites')
 prerequisites = c.fetchall()

 c.execute('SELECT * FROM majors')
 majors = c.fetchall()

 conn.close()
'''

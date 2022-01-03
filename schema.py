import sqlite3

#create a connection 
connection = sqlite3.connect('flask_tut.db', check_same_thread = False)

#insert a cursor object
cursor = connection.cursor()

#create a table with cursor 
cursor.execute(
	#insert sqlite3 command
	"""CREATE TABLE users(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		username VARCHAR(16),
		password VARCHAR(32),
		favourite_color VARCHAR(32)
	);"""

)

connection.commit()
cursor.close()
connection.close()

import sqlite3

#create a connection 
connection = sqlite3.connect('flask_tut.db', check_same_thread = False)

#insert a cursor object
cursor = connection.cursor()

#create a table with cursor 
cursor.execute(
	#insert sqlite3 command
	"""INSERT INTO users(
		username,
		password,
		favourite_color
		)VALUES(
			'user',
			'pass',
			'Red'
			),
			(
			'mike',
			'pass',
			'Blue'
			),
			(
			'gab',
			'pass',
			'Black'
	);"""
)

connection.commit()
cursor.close()
connection.close()

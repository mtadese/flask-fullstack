import sqlite3 

def show_color(username):
	connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
	cursor = connection.cursor()

	cursor.execute(""" SELECT favourite_color FROM users WHERE username = '{username}' ORDER BY pk DESC;""".format(username = username))
	color = cursor.fetchone()[0]

	connection.commit()
	cursor.close()
	connection.close()

	message = '{username}\'s favourite color is {color}.'.format(username=username, color=color)

	return message

#create a function to check the password
def check_pw(username):
	connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
	cursor = connection.cursor()

	cursor.execute(""" SELECT password FROM users WHERE username = '{username}' ORDER BY pk DESC;""".format(username = username))

	password = cursor.fetchone()[0]

	connection.commit()
	cursor.close()
	connection.close()

	return password


#create function to signup new user
def signup(username, password, favourite_color):
	connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
	cursor = connection.cursor()

	#check if registering user is not already existing in the database
	cursor.execute("""SELECT password FROM users WHERE username = '{username}';""".format(username = username))

	exist = cursor.fetchone()

	if exist is None:
		cursor.execute("""INSERT INTO users(username, password, favourite_color)VALUES('{username}', '{password}', '{favourite_color}');""".format(username=username, password=password, favourite_color=favourite_color))

		connection.commit()
		cursor.close()
		connection.close()

	else:
		return ('User already signed up')

	return 'You have successfully signed up!!!'


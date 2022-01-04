from flask import Flask, render_template, request
import model

#create an app
app = Flask(__name__)

#create a route for the flask app (homepage)
@app.route('/', methods = ['GET', 'POST'])

#create a home function
def home():
	if request.method == 'GET':
		return render_template('index.html', message='Welcome to the Homepage')
	else:
		username = request.form['username']
		password = request.form['password']
		db_password = model.check_pw(username)

		if password == db_password:
			message = model.show_color(username)

			return render_template('football.html', message = message)
		else:
			error_message = 'Hint: username is similar to user'
			return render_template('index.html', message = error_message)

#create a route for the flask app (football page)
@app.route('/football', methods = ['GET'])

#create a football function
def football():
	return render_template('football.html')

#create a route for the flask app (signup page)
@app.route('/signup', methods = ['GET', 'POST'])

#create a signup function
def signup():
	if request.method == 'GET':
		message = 'Signup Here!'
		return render_template('signup.html', message = message)
	else:
		username = request.form["username"]
		password = request.form["password"]
		favourite_color = request.form["favourite_color"]

		message = model.signup(username, password, favourite_color)
		return render_template('signup.html', message = message)

#run the app on a preferred port
if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 7000, debug= True)


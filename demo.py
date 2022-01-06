from flask import Flask, render_template, request, session, redirect, url_for, g
import model

#create an app
app = Flask(__name__)

#declare a secret key
app.secret_key = 'sample_key'

username = ''
user = model.check_users()

#create a route for the flask app (homepage)
@app.route('/', methods = ['GET'])

#create a home function
def home():
	if 'username' in session:
	#declare the global variable (g) for flask
		g.user =session['username']
		return render_template('football.html', message = '<img src= static/img/coffee.jpg>')
	return render_template('homepage.html', message = 'Login to the page or Signup')

@app.route('/login', methods=['GET', 'POST'])
def login():
	#if another user logs in while a previous user is logged in n same system, the previous user will be popped out
	if request.method == 'POST':
		session.pop('username', None)
		areyouuser = request.form['username']
		pwd = model.check_pw(areyouuser)
		if request.form['password'] == pwd:
			session['username'] = request.form['username']
			#redirect to the home function
			return redirect(url_for('home'))
	return render_template('index.html')


"""	if request.method == 'GET':
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
"""

@app.before_request
def before_request():
	g.username = None
	if 'username' in session:
		g.username = session['username']



"""
#create a route for the flask app (football page)
@app.route('/football', methods = ['GET'])

#create a football function
def football():
	return render_template('football.html')
"""

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

@app.route('/getsession')
def get_session():
	if 'username' in session:
		return session['username']
	return redirect(url_for('login'))

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('home'))

#run the app on a preferred port
if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 7000, debug= True)

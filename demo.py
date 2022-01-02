from flask import Flask, render_template, request

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

		if username == 'user' and password == 'pass' :
			return render_template('football.html', message = 'Login Successful')
		else:
			error_message = 'Hint: username is similar to user'
			return render_template('index.html', message = error_message)

#create a route for the flask app (football page)
@app.route('/football', methods = ['GET'])

#create a football function
def football():
	return render_template('football.html')

#run the app on a preferred port
if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 7000, debug= True)


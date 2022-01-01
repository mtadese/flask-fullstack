from flask import Flask, render_template

#create an app
app = Flask(__name__)

#create a route for the flask app (homepage)
@app.route('/', methods = ['GET'])

#create a home function
def home():
	return render_template('index.html')

#create a route for the flask app (football page)
@app.route('/football', methods = ['GET'])

#create a football function
def football():
	return render_template('football.html')

#run the app on a preferred port
if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 7000, debug= True)


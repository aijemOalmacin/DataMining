# pip install flask
# pip install flask-cors
from flask import Flask, request, Response, render_template
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

def the_model(speed, type, Gender, beginner, passenger):
	result_str = ''
	with open('logistic.pk', 'rb') as f:
		model = pickle.load(f)
		type = 1 if type == 'yes' else 0
		Gender = 1 if Gender == 'yes' else 0
		beginner = 1 if beginner == 'yes' else 0
		output = model.predict_proba([[speed, type, Gender, beginner, passenger]])
		result_str += "Safe " + "{:.4f}".format(output[0][0]) + "<br />"
		result_str += "Not " + "{:.4f}".format(output[0][1]) + "<br />"
	return result_str

@app.route('/sample-url', methods=['GET'])
def sample_url():
	return render_template('sample-url.html')

@app.route('/input', methods=['GET'])
def input():
	return render_template('input.html')

@app.route('/model-api', methods=['POST'])
def model_api():
	speed = request.form.get('speed')
	type = request.form.get('type')
	Gender = request.form.get('Gender')
	beginner = request.form.get('beginner')
	speed =float(speed)
	passenger = request.form.get('passenger')
	passenger = int(passenger)
	the_output = the_model(speed, type, Gender, beginner, passenger)
	return the_output

if __name__ == '__main__':
	app.run(debug=True, port='8080', host='0.0.0.0', use_reloader=True)
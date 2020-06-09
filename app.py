from flask import Flask, render_template, request, jsonify
from xorCipher import cipher
from predict import decode_sequence, process_text

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/handle_data', methods=['POST'])
def _get_data():
    message = request.form['message']
    result = compute_cipher(message)
    prediction = compute_prediction(result)
    accuracy = compute_accuracy(message, prediction)
    return render_template('index.html',
    	message=message, result=result, prediction=prediction, accuracy=accuracy)


def compute_cipher(message):
	result = cipher(message)
	return result


def compute_prediction(toDecode):
	res = decode_sequence(process_text(toDecode), len(toDecode))
	return res


def compute_accuracy(message, predition):
	same = 0
	for u, v in zip(message, predition):
		if u == v:
			same += 1
	ratio = same / len(message)
	percentage = ratio * 100
	return round(percentage, 2)


if __name__ == '__main__':
	app.run(debug=False)

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
    return render_template('index.html',
    	message=message, result=result, prediction=prediction)


def compute_cipher(message):
	result = cipher(message)
	return result

def compute_prediction(toDecode):
	res = decode_sequence(process_text(toDecode))
	return res


if __name__ == '__main__':
	app.run(debug=False)

from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def user():
	data = request.get_json()
	return data

@app.route('/books')
def books():
	return jsonify({ "books": [ { 'name': 'A arte de se fuder', 'price': '15,00R$' }, { 'name': 'A arte de se dar bem', 'price': '15,00R$' } ] })


app.run()
from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers import getUser, getChat

app = Flask(__name__, static_folder='.')
CORS(app)

@app.route("/")
def root():
    return app.send_static_file("./index.html")

@app.route("/profile", methods=["GET","POST","PUT"])
def profile():
	response, code = getUser(request)
	return jsonify(response), code

@app.route("/chat", methods=["GET","POST","PUT"])
def chat():
	response, code = getChat(request)
	return jsonify(response), code

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='3000')
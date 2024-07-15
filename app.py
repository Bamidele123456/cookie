from flask import Flask, request, make_response, jsonify, render_template
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/index')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def reg():
    email = request.form['email']
    password = request.form['password']
    user_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, email))
    response = make_response(jsonify({'message': 'Registration successful'}))
    response.set_cookie('user_id', user_id)
    return response, 200


@app.route('/send_user_id', methods=['GET'])
def receive_user_id():
    user_id = request.args.get('user_id')
    print(f"Received user_id: {user_id}")
    return "User ID received"


if __name__ == '__main__':
    app.run(debug=True)

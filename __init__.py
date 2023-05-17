from flask import Flask, jsonify, render_template, request, abort, make_response
from markupsafe import escape
from flask_restful import Resource, Api, reqparse
import os.path

errors = {"PageNotFound": {"Message": "Page doesnt exist", "status": 404}}
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument("id", type=int)
parser.add_argument("command", type=str)
"""
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/script/<name>')
def hell(name):
    if os.path.isfile(f'./templates/script/{name}'):
        return render_template(f'/script/{name}')
    else:
        abort(404)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
"""

parser = reqparse.RequestParser()
parser.add_argument(
    'foo',
    choices=('one', 'two'),
    help='Bad choice: {error_msg}'
)

parser = reqparse.RequestParser()
parser.add_argument('login', type=str)
parser.add_argument("pass", type=str)
#parser.add_argument("command", type=str)

class Worksheet(Resource):
    def post(self):
        print("PostWs arrived")
        args = parser.parse_args()
        print(args['login'], args['pass'])
        return jsonify("{}")

    def get(self):
        print("GetWS arrived")
        return make_response(render_template('acc.html'))
class Login(Resource):
    def post(self):
        print("Post Login arrived")
        args = parser.parse_args()
        print(args)
        return jsonify("{}")
    def get(self):
        print("Get Login arrived")
        return make_response(render_template('login.html'))
class SignUp(Resource):
    def get(self):
        return make_response(render_template('registration.html'))

api.add_resource(Worksheet, '/')
api.add_resource(Login, '/login')
api.add_resource(SignUp, '/registration')



if __name__ == '__main__':
    app.run(debug=True)

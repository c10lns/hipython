from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def signin_form():
    return 'user: csh'

def registe():
    print('user registe')
    app.run()
from flask import Flask, request
import pymysql
import db_connector
import os
import signal

app = Flask(__name__)

# local users storage
users = {}
# supported methods
@app.route('/us/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        if db_connector.user_get(user_id):
            return {'status': 'ok', 'user_name': db_connector.user_get(user_id) }, 200
        else:
            return {'status': 'error', 'reason': 'no such id'}, 500
           # return {'status1': 'error', 'reason': 'no_such_id' }, 500
    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        users[user_id] = user_name
        if (db_connector.user_post(user_id, user_name)):
            return {'status': 'ok', 'user_added': user_id , 'user name': user_name}, 200
        else:
            return {'status': 'error', 'reason': 'user already exist'}, 500
    elif request.method == 'DELETE':
        if db_connector.user_del(user_id):
            return {'status': 'ok', 'user deleted': user_id} , 200
        else:
            return {'status': 'error', 'reason': 'no such user_id'}, 500
    elif request.method == 'PUT':
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        users[user_id] = user_name
        if db_connector.user_put(user_id,user_name):
            return {'status': 'ok', 'user updated': user_name} , 200
        else:
            return {'status': 'error', 'reason': 'no such id '+ user_id}, 500

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'
# status code
  # todo elif for put and delete


app.run(host='127.0.0.1', debug=True, port=5000)





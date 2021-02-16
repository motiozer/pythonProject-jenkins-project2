from flask import Flask, request
import pymysql
import db_connector
import os
import signal

app = Flask(__name__)

# local users storage
users = {}
# supported methods
@app.route('/users/get_user_name/<user_id>')
def get_user_name(user_id):
    if db_connector.user_get(user_id):
        user_name = db_connector.user_get(user_id)
        return "<H1 id='user'>" + user_name + "</H1>"
    else:
        return "<H1 id='error'>" + 'no such user: ' + user_id + "</H1>"

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5001)




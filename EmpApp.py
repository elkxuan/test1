from flask import Flask, render_template, request
from pymysql import connections
import os
import pymysql
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'employee'


@app.route('/')
def Index():
    conn = db_conn
    cur = conn.cursor(pymysql.cursors.DictCursor)
 
    cur.execute('SELECT * FROM employee')
    data = cur.fetchall()
  
    cur.close()
    return render_template('index.html', employee = data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

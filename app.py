from flask import Flask
import psycopg2


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! from emdonkus in 3308'

@app.route('/db_test')
def hello_world():
    conn = psycopg2.connect('postgres://lab_10_db_9z0p_user:7j7l6zcs6J720w5CgLnvnPb8FAXjX01q@dpg-cnpel16n7f5s73c4pjeg-a/lab_10_db_9z0p')
    
    
    conn.close()
    return "Database Connection Successful"

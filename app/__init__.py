from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'cookie dough'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'traxex23999'
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

from app import routes
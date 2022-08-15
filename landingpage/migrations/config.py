from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'training'
app.config['MYSQL_DATABASE_PASSWORD'] = 'training'
app.config['MYSQL_DATABASE_DB'] = 'retail_db'
app.config['MYSQL_DATABASE_HOST'] = '188.166.221.246'
mysql.init_app(app)
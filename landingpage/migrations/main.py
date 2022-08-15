import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/dept')
def dept():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT department_id, department_name FROM departments")
        deptRows = cursor.fetchall()
        respone = jsonify(deptRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/dept/<department_id>')
def dept_details(department_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT  department_name FROM departments WHERE department_id =%s", department_id)
        deptRow = cursor.fetchone()
        respone = jsonify(deptRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 
        
       
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port =8005, debug = True)
    app.run()
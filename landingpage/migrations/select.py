# importing required libraries
import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="188.166.221.246",
  user ="training",
  passwd ="training",
  database = "retail_db"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
  
query = "SELECT department_id,  department_name FROM departments"
cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)
 
# disconnecting from server
dataBase.close()
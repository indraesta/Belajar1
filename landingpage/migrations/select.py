# importing required libraries
import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="188.166.221.246",
  user ="training",
  passwd ="training",
  database = ""
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
  
query = "SELECT **,  ** FROM **"
cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)
 
# disconnecting from server
dataBase.close()
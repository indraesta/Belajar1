import mysql.connector
  
#Establishing connection
conn = mysql.connector.connect(
		user="training",
        host="188.166.221.246",
        password ="training",
        database=""
		)
  
# Creating a cursor object using
# the cursor() method
mycursor = conn.cursor();
  
# SQL Query
sql = "select * from ** where ** >= 3;"
  
# Executing query
mycursor.execute(sql)
  
myresult = mycursor.fetchall()
  
for x in myresult:
    print(x)
 
# Closing the connection
conn.close()
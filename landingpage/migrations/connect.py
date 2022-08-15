# importing required libraries
import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="188.166.221.246",
  user ="training",
  passwd ="training"
)
 
print(dataBase)
  
# Disconnecting from the server
dataBase.close()
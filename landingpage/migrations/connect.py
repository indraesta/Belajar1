# importing required libraries
import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="188.166.221.246",
  user ="training",
  passwd ="training"
)

if dataBase.is_connected();
print("Berhasil connect"dataBase)


# Disconnecting from the server
dataBase.close()
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="elias_admin",
  password="Rufus1234",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

print(mycursor.rowcount, "record inserted.")

mycursor.close()
mydb.close()

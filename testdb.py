# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="userB",
        password="a_p@55w0rd",
        host="127.0.0.1",
        port=3306,
        database="myIoTDB"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
mycursor = conn.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)


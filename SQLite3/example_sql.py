import sqlite3

cursor = sqlite3.connect("C:\\Users\\vaibhav.gawande\\PycharmProjects\\pateint_db.db")

data = cursor.execute("SELECT * FROM Patient_Data")
for i in data:
    print(i)
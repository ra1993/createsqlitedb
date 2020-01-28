import sqlite3
import csv

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")

cursor.execute("""

CREATE TABLE "employees"(
"users" TEXT (20),
"email" TEXT (32),
"country" TEXT (32)
)

""")

with open("employees.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        #print(row)
        users = row[0]
        email = row[4]
        country = row[5]
        cursor.execute("""INSERT INTO employees(users, email, country) VALUES(?,?,?)""",
        (users, email, country))

    conn.commit()
#-----------------------------------------------------------------
cursor.execute("DROP TABLE IF EXISTS phone_numbers")

cursor.execute("""
CREATE TABLE "phone_numbers"(
"users" TEXT (20),
"cell_phone" TEXT (20),
"home_phone" TEXT (20),
"work_phone" TEXT (20)
)
""")

with open("employees.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        #print(row)
        users = row[0]
        cell_phone = row[1]
        home_phone = row[2]
        work_phone = row[3]
        cursor.execute("""INSERT INTO employees(users, cell_phone, home_phone, work_phone) VALUES(?,?,?,?)""",
        (users, cell_phone, home_phone, work_phone))

    conn.commit()

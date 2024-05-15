import mysql.connector
from mysql.connector import errorcode

def fetch_data(query):
    try:
        db = mysql.connector.connect(
            user="root",
            password="popcorn",
            host="127.0.0.1",
            database="bacchus",
            raise_on_warnings=True
        )
        cursor = db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        db.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Please check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(err)

# SELECT queries
queries = {
    "Employees": "SELECT * FROM Employees",
    "Suppliers": "SELECT * FROM Suppliers",
    "Products": "SELECT * FROM Products",
    "Orders": "SELECT * FROM Orders",
    "Shipments": "SELECT * FROM Shipments",
    "Distributors": "SELECT * FROM Distributors",
    "EmployeeHours": "SELECT * FROM EmployeeHours"
}

# Fetch and print data from each table
for table, query in queries.items():
    print(f"\nData from {table}:")
    fetch_data(query)

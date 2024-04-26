import mysql.connector
from mysql.connector import errorcode

config = {    
    "user": "root",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\nPress any key to continue...")

    # First query: Select all fields for the studio table
    cursor = db.cursor()
    query = "SELECT * FROM studio"
    cursor.execute(query)
    print("\nQuery 1: All fields for the studio table")
    for row in cursor.fetchall():
        print(row)

    # Second query: Select all fields for the genre table
    query = "SELECT * FROM genre"
    cursor.execute(query)
    print("\nQuery 2: All fields for the genre table")
    for row in cursor.fetchall():
        print(row)

    # Third query: Select movie names for movies with a run time of less than two hours
    query = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120"
    cursor.execute(query)
    print("\nQuery 3: Movie names for movies with a run time of less than two hours")
    for row in cursor.fetchall():
        print(row[0])

    # Fourth query: Get a list of film names and directors grouped by director
    query = "SELECT MAX(film_name) AS film_name, film_director FROM film GROUP BY film_director"
    cursor.execute(query)
    print("\nQuery 4: Film names and directors grouped by director")
    for row in cursor.fetchall():
        print("Director:", row[1])
        print("Films:", row[0])
        print(row[0])

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
        
    else:
        print(err)
        
finally:
    if 'db' in locals() and db.is_connected():
        db.close()
        print("MySQL connection is closed")

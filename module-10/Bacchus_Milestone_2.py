import mysql.connector
from mysql.connector import errorcode

# Connect to MySQL database
try:
    # Establish database connection
    db = mysql.connector.connect(
        user="root",
        password="popcorn",
        host="127.0.0.1",
        database="bacchus",
        raise_on_warnings=True
    )
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format("root", "127.0.0.1", "movies"))
    input("\nPress any key to continue...")
    cursor = db.cursor()

    # Define table creation queries
    create_tables_query = [
        """
        CREATE TABLE Employees (
            employee_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            department VARCHAR(255),
            title VARCHAR(255)
        )
        """,
        """
        CREATE TABLE Suppliers (
            supplier_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            product_type VARCHAR(255),
            delivery_frequency VARCHAR(255)
        )
        """,
        """
        CREATE TABLE Products (
            product_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            type VARCHAR(255)
        )
        """,
        """
        CREATE TABLE Orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            supplier_id INT,
            quantity INT,
            order_date DATE,
            FOREIGN KEY (product_id) REFERENCES Products(product_id),
            FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
        )
        """,
        """
        CREATE TABLE Shipments (
            shipment_id INT AUTO_INCREMENT PRIMARY KEY,
            supplier_id INT,
            expected_delivery DATE,
            actual_delivery DATE,
            FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
        )
        """,
        """
        CREATE TABLE Distributors (
            distributor_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            product_id INT,
            FOREIGN KEY (product_id) REFERENCES Products(product_id)
        )
        """,
        """
        CREATE TABLE EmployeeHours (
            employee_id INT,
            quarter INT,
            hours_worked INT,
            FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
        )
        """
    ]

    # Execute table creation queries
    for query in create_tables_query:
        cursor.execute(query)
    db.commit()

    # Populate tables with sample data
    # Insert statements for each table

    # Display data in each table
    # Select statements for each table

# Define insert statements for each table
    employees_data = [
        ("Jane vu", "Finance", "Financial Analyst"),
        ("Margaret Murphy", "Marketing", "Marketing Head"),
        ("Krish bob", "Marketing", "Assistant"),
        ("David Doyle", "Production", "Production Manager"),
        ("John Sexton", "Distribution", "Distribution Manager"),
        ("Charles Waston", "Supply", "Supply Manager")
    ]
    suppliers_data = [
        ("Supplier A", "Blue and Red", "Monthly"),
        ("Supplier B", "Sky and Moon", "Monthly"),
        ("Supplier C", "Yellow and Boxes", "Monthly")
    ]
    products_data = [
        ("Pinot noir", "Red Wine"),
        ("Syrah", "Red Wine"),
        ("Riesling", "White Wine"),
        ("Chardonnay", "White Wine")
    ]
    distributors_data = [
        ("Distributor 1", 1),  # Distributor 1 carries Pinot noir
        ("Distributor 2", 2),  # Distributor 2 carries Syrah
        ("Distributor 3", 3),  # Distributor 3 carries Riesling
        ("Distributor 4", 4)   # Distributor 4 carries Chardonnay
    ]
    
    # Execute insert statements for each table
    cursor.executemany("INSERT INTO Employees (name, department, title) VALUES (%s, %s, %s)", employees_data)
    cursor.executemany("INSERT INTO Suppliers (name, product_type, delivery_frequency) VALUES (%s, %s, %s)", suppliers_data)
    cursor.executemany("INSERT INTO Products (name, type) VALUES (%s, %s)", products_data)
    cursor.executemany("INSERT INTO Distributors (name, product_id) VALUES (%s, %s)", distributors_data)


    # Commit changes to the database
    db.commit()


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied. Please check your username and password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: Database does not exist.")
    else:
        print(err)

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()

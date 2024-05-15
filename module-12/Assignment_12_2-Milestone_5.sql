-- setup_bacchus_db.sql

CREATE TABLE Employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    department VARCHAR(255),
    title VARCHAR(255)
);

CREATE TABLE Suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    product_type VARCHAR(255),
    delivery_frequency VARCHAR(255)
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255)
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    supplier_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Shipments (
    shipment_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_id INT,
    expected_delivery DATE,
    actual_delivery DATE,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Distributors (
    distributor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE EmployeeHours (
    employee_id INT,
    quarter INT,
    hours_worked INT,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

-- Insert data
INSERT INTO Employees (name, department, title) VALUES
('Jane Vu', 'Finance', 'Financial Analyst'),
('Margaret Murphy', 'Marketing', 'Marketing Head'),
('Krish Bob', 'Marketing', 'Assistant'),
('David Doyle', 'Production', 'Production Manager'),
('John Sexton', 'Distribution', 'Distribution Manager'),
('Charles Watson', 'Supply', 'Supply Manager');

INSERT INTO Suppliers (name, product_type, delivery_frequency) VALUES
('Supplier A', 'Blue and Red', 'Monthly'),
('Supplier B', 'Sky and Moon', 'Monthly'),
('Supplier C', 'Yellow and Boxes', 'Monthly');

INSERT INTO Products (name, type) VALUES
('Pinot Noir', 'Red Wine'),
('Syrah', 'Red Wine'),
('Riesling', 'White Wine'),
('Chardonnay', 'White Wine');

INSERT INTO Distributors (name, product_id) VALUES
('Distributor 1', 1),
('Distributor 2', 2),
('Distributor 3', 3),
('Distributor 4', 4);

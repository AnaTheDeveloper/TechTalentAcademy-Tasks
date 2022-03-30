# • The Structured Query Language (SQL) is specially designed to communicate with databases.
# • SQL is the industry-wide standard language used by most relational database systems.
# • SQL is used for creating, accessing and manipulating databases. It allows you to store, search, update, edit,
# retrieve and delete data from a database.
# • Some common relational database management systems that use SQL are: Oracle, Sybase, Microsoft SQL Server, Access, PostgreSQL, etc.

# Relational Database Keywords.
# Database: all the of the table structure and records saved.
# Table: holds all of the data and information of the databases. This is organised in rows and columns.
# Fieldnames: column headings (variable names).
# Datatypes: assigned to fields to store the correct type of data.
# Records: is when all the fields are completed for one entity.

# Foreign keys are created when a primary key from one table appears in another table.

# Workbench is a software tool used to access MySQL using an intuitive/friendly user interface (rather than command line). The
# command line can be more difficult for novice users to use.
# A user enters sql commands via a command line or the workbench that connects to your SQL server.

# Datatypes in SQL

# Type Value
# CHAR() A FIXED length string (can contain letters, numbers, and special characters). The size parameter()
# specifies the column length in characters - can be from 0 to 255. Default is 1. E.g. CHAR(10) will
# allow 10 characters.
# VARCHAR() A string of variable length up to 255 characters long.
# INT An integer range is from -2147483648 to 2147483647.
# DECIMAL A floating point number that can specify the number permissible digits. E.g. (5,2) permits – 999.99
# to 999.99.
# DOUBLE A long double-precision floating point number.
# DATE A date in the YY-MM-DD format.
# TIME A time in the HH:MM:SS format.
# DATETIME Combination of the date and time format. Date first and then time. YY-MM-DD HH:MM:SS
# YEAR A year 1901-2155 in either YY of YYYY format.
# TEXT A string up to 65,535 characters long.
# BLOB A binary type for variable data.
# ENUM A single string value from defined list. For example, ENUM(“Dr”, “Mr”, “Mrs”).
# SET A single/multiple strings value from defined list. For example, ENUM(“Red”, “Green”, “Yellow”).
# BOOL Equal to Boolean.

# Datatypes in SQL
# Type Value
# NOT NULL Insists that no data can be blank – must have a data value in the column.
# UNIQUE Ensure that records may not duplicate any entry in this column.
# AUTO_INCREMENT On numeric columns that automatically generates a number one more than the previous numbers in the column.
# DEFAULT Specifies a value to be used where no value is entered for the column when inserting records.
# PRIMARY KEY Specifies when column will be used as the primary key for that table.

# • (INNER) JOIN: Returns records that have matching values in both tables.
# • LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table.
# • RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table.
# • FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table.

# Example from SQL Text File converted to work in Pycharm
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="ordering_system")

# To connect to an existing database add on database="database_name".

cursor = db.cursor()

# Creating a new database.
cursor.execute('''CREATE DATABASE ordering_system''')

# Checking if the database already exists.
cursor.execute("SHOW DATABASES")

# Creating a new table.
cursor.execute('''CREATE TABLE customers(
                    CustomerID INT PRIMARY KEY,
                    CustomerName VARCHAR(100),
                    ContactName VARCHAR(100),
                    Address VARCHAR(100),
                    City VARCHAR(80),
                    PostalCode VARCHAR(10),
                    Country VARCHAR(40))''')

# See what your database looks like so far.
# cursor.execute('''EXPLAIN customers''')

# Enter data into the table.
cursor.execute('''INSERT INTO customers VALUES (
                    (1, "Toby Flunderson", "James", "Jammy Dogdger Avenue", "Scranton", "12209", "USA"),
                    (2, "Leslie Knope", "James", "Custard Cream Boulevard", "Pawnee", "05021", "USA"),
                    (3, "Dwight Schrute", "James", "Wagon Wheel Place", "Scranton", "122541", "USA"),
                    (4, "Donna Meagle", "James", "Leibniz Lane", "Pawnee", "05020", "USA"),
                    (5, "April Ludgate", "James", "Digestive Road", "Pawnee", "01756", "USA"),
                    (6, "Stanley Hudson", "James", "Hobnob Street", "Scranton","122554", "USA"))''')

# ALTERNATIVE METHOD
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# Commit changes to database
db.commit()

# Creating second table.
cursor.execute('''CREATE TABLE orders(
                      OrderID INT NOT NULL PRIMARY KEY,
                      CustomerID INT,
                      ItemID INT NOT NULL,
                      ItemName VARCHAR(80))''')

# Update a column.
cursor.execute('''ALTER TABLE orders ADD ProductPrice DECIMAL(6,2)''')

# Add data into second table.
cursor.execute('''INSERT INTO orders VALUES (
                    (6, 5021545, 32174524,  "Toaster",  17.99),
                    (3, 5021546, 45142548, "Set of 3 Nested Tables", 105.99),
                    (3, 5021547, 87413547, "Electric Toothbrush", 45.99),
                    (1, 5021548, 24586596, "4 Person Tent", 220.99),
                    (4, 5021549, 47512543, "Upright Fan", 41.99),
                    (5, 5021550, 73519487, "Henry Hoover", 111.99))''')

# Commit changes to database
db.commit()

# Return all rows.
cursor.execute("SELECT * FROM orders").fetchall()

# Update specific row
cursor.execute('''UPDATE orders SET ProductPrice = 119.99 WHERE OrderID = 5021550''')

# Return all rows.
cursor.execute("SELECT * FROM orders").fetchall()

# Joining Tables
cursor.execute('''SELECT customers.CustomerName , orders.OrderID FROM customers
                    INNER JOIN orders
                    ON customers.CustomerID = orders.CustomerID''')

# Selecting specific information
cursor.execute('''SELECT * FROM customers
                    INNER JOIN orders
                    WHERE customers.CustomerID = orders.CustomerID AND orders.ItemName = "Toaster"''')

cursor.execute('''SELECT * FROM orders WHERE ProductPrice between 35 and 120''')

cursor.execute('''UPDATE customers SET CustomerName = 'Pam Beesley' WHERE CustomerId = 4''')

# Return all rows.
cursor.execute("SELECT * FROM customers").fetchall()

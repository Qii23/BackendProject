import connection
from datetime import datetime
from flask import Flask

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE User (ID int Primary key AUTO_INCREMENT, name VARCHAR(50), gender VARCHAR(10), role ENUM('Staff','Client'))")
mycursor.execute("CREATE TABLE Product (ID int Primary key AUTO_INCREMENT, name VARCHAR(50), quantity INT default 0, price INT)")
mycursor.execute("CREATE TABLE DetailProduct (productID int PRIMARY KEY, FOREIGN KEY (productID) REFERENCES Product(ID), picture text, description VARCHAR(100))")
mycursor.execute("CREATE TABLE Store (ID int Primary key AUTO_INCREMENT, name VARCHAR(50), address VARCHAR(50))")
mycursor.execute("CREATE TABLE HeaderTransaction (ID int Primary key AUTO_INCREMENT, storeID INT, FOREIGN KEY(storeID) REFERENCES Store(ID), total INT, created datetime)")
mycursor.execute("CREATE TABLE DetailTransaction (ID int Primary key AUTO_INCREMENT, headerID int, FOREIGN KEY(headerID) REFERENCES HeaderTransaction(ID), productID int, FOREIGN KEY(productID) REFERENCES Product(ID), quantity INT)")
mycursor.execute("CREATE TABLE Attendance (ID int primary key AUTO_INCREMENT, userID int, FOREIGN KEY(userID) REFERENCES User(ID), inTime datetime)")
mycursor.execute("ALTER TABLE HeaderTransaction add (userID int, FOREIGN KEY (userID) REFERENCES User(ID))")

mycursor.execute("INSERT INTO User (name,gender,role) VALUES (%s,%s,%s)", ("rafqi", "male", "Staff"))
mycursor.execute("INSERT INTO User (name,gender,role) VALUES (%s,%s,%s)", ("dabun", "male", "Client"))
mycursor.execute("INSERT INTO User (name,gender,role) VALUES (%s,%s,%s)", ("asep", "male", "Client"))
mycursor.execute("INSERT INTO User (name,gender,role) VALUES (%s,%s,%s)", ("susi", "female", "Client"))
mydb.commit()
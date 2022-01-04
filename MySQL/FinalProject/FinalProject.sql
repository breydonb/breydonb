CREATE TABLE sales(
    CustomerId int NOT NULL PRIMARY KEY,
    FirstName VARCHAR2(255) NOT NULL,
    LastName VARCHAR2(20) NOT NULL,
    Address VARCHAR2(255) NOT NULL,
    City VARCHAR2(255) NOT NULL,
    StateInitials CHAR(2) NOT NULL,
    Country VARCHAR2(255) NOT NULL,
    ZipCode VARCHAR2(10) NOT NULL,
    ProductName VARCHAR2(255) NOT NULL,
    ItemNumber NUMBER(10) NOT NULL,
    ProductPrice NUMBER(19,4) NOT NULL,
    OrderDate DATE NOT NULL,
    OrderNumber NUMBER(10) NOT NULL,
    FOREIGN KEY(CustomerId) REFERENCES Customers(CustomerId)
);

CREATE TABLE SalesHistory();

SELECT CUSTOMERID ,FIRSTNAME ,LASTNAME ,ADDRESS ,CITY ,STATEINITIALS ,COUNTRY ,ZIPCODE ,PRODUCTNAME ,ITEMNUMBER ,PRODUCTPRICE ,ORDERDATE ,ORDERNUMBER INTO ap.SalesHistory FROM sales WHERE rownum <= 3 ORDER BY rownum DESC;

CREATE TABLE SalesHistory(
    CustomerId int NOT NULL PRIMARY KEY,
    FirstName VARCHAR2(255) NOT NULL,
    LastName VARCHAR2(20) NOT NULL,
    Address VARCHAR2(255) NOT NULL,
    City VARCHAR2(255) NOT NULL,
    StateInitials CHAR(2) NOT NULL,
    Country VARCHAR2(255) NOT NULL,
    ZipCode VARCHAR2(10) NOT NULL,
    ProductName VARCHAR2(255) NOT NULL,
    ItemNumber NUMBER(10) NOT NULL,
    ProductPrice NUMBER(19,4) NOT NULL,
    OrderDate DATE NOT NULL,
    OrderNumber NUMBER(10) NOT NULL
);

DROP TABLE SalesHistory;

INSERT INTO SALESHISTORY SELECT * FROM s WHERE rownum <= 3;

SELECT * FROM sales WHERE rownum <= 3 ORDER BY rownum DESC;

SELECT * FROM SALESHISTORY;

INSERT INTO sales VALUES(100, 'John', 'Cena', '123 Ucantseeme St', 'West Newbury', 'MA', 'United States', '45823', 'Aqua Tofana',830238, 99.99, sysdate, 17245243);
INSERT INTO sales VALUES(sales_seq.nextval,'Timmy', 'Turner', '500 Wish Ave', 'Pixie', 'TX', 'United States', '74842', 'Maples Apple Sauce', 94857, 6.99, sysdate, 18742534);
INSERT INTO sales VALUES(sales_seq.nextval,'Santa', 'Clause', '1221 Red Nose St.', 'North Pole', 'WY', 'United States', '48726', 'All-Purpose Rope', 923847, 50.00, sysdate, 51234895);
INSERT INTO sales VALUES(sales_seq.nextval, 'Parker', 'Peter', '20 Ingram St', 'Queens', 'NY', 'United States', '57892', 'Stabby Knife', 39847, 100.00, sysdate, 48763529);
INSERT INTO sales VALUES(sales_seq.nextval, 'Santa', 'Clause', '1221 Red Nose St.', 'North Pole', 'WY', 'United States', '48726', 'Stabby Knife', 39847, 100.00, sysdate, 48763529);
INSERT INTO sales VALUES(sales_seq.nextval, 'John', 'Cena', '123 Ucantseeme St', 'West Newbury', 'MA', 'United States', '45823', 'Maples Apple Sauce', 94857, 6.99, sysdate, 18742534);
INSERT INTO sales VALUES(sales_seq.nextval, 'Timmy', 'Turner', '500 Wish Ave', 'Pixie', 'TX', 'United States', '74842', 'All-Purpose Rope', 923847, 50.00, sysdate, 51234895);
INSERT INTO sales VALUES(sales_seq.nextval, 'Parker', 'Peter', '20 Ingram St', 'Queens', 'NY', 'United States', '57892', 'Stabby Knife', 39847, 100.00, sysdate, 48763529);
INSERT INTO sales VALUES(sales_seq.nextval, 'Santa', 'Clause', '1221 Red Nose St.', 'North Pole', 'WY', 'United States', '48726', 'Aqua Tofana',830238, 99.99, sysdate, 17245243);
INSERT INTO sales VALUES(sales_seq.nextval, 'John', 'Cena', '123 Ucantseeme St', 'West Newbury', 'MA', 'United States', '45823', 'All-Purpose Rope', 923847, 50.00, sysdate, 51234895);
INSERT INTO sales VALUES(sales_seq.nextval, 'Timmy', 'Turner', '500 Wish Ave', 'Pixie', 'TX', 'United States', '74842', 'Maples Apple Sauce', 94857, 6.99, sysdate, 18742534);

UPDATE sales SET CustomerID = 109 WHERE CustomerID = 111


CREATE SEQUENCE Customer_seq start with 101 increment by 1 maxvalue 200 nocycle nocache;
DROP SEQUENCE Customer_seq;

CREATE SEQUENCE sales_seq start with 101 increment by 1 maxvalue 200 nocycle nocache;
CREATE SEQUENCE Customer_seq start with 100 increment by 1 maxvalue 200 nocycle nocache;

INSERT INTO products VALUES (830238, 'Aqua Tofana', '1000', 99.99, 'Giulia Tofana Inc.');
INSERT INTO products VALUES (923847, 'All-Purpose Rope', 1, 50.00, 'Harvey Glatman Rope Shop');
INSERT INTO products VALUES (39847, 'Stabby Knife', '177', 100.00, 'Bergamos Bargain Knives');
INSERT INTO products VALUES (303847, 'Kidnappers Select Padlock', 200, 43.99, 'Kohlhepps Kidnapping Supplies');
INSERT INTO products VALUES (303847, 'Kidnappers Select Padlock', 200, 43.99, 'Kohlhepps Kidnapping Supplies');

SELECT * FROM products;
  
  
DROP SEQUENCE sales_seq;


DROP TABLE sales;

CREATE TABLE Customers(
    CustomerId int primary key,
    FirstName varchar2(20),
    LastName varchar2(20),
    Address varchar2(40),
    City char(15),
    State char(2),
    PhoneNumber char(10),
    Email varchar2(30),
    AmazonPrime char(12),
    DateOfJoining date default sysdate
);

CREATE SYNONYM s FOR sales;

SELECT * from s;

DROP TABLE Customers;

SELECT * FROM products;
    
CREATE TABLE products (
    ProductID int NOT NULL,
    ProductName varchar(255),
    ProductStock varchar(255),
    ProductPrice NUMBER(19,4),
    ProductSeller varchar(255),
    PRIMARY KEY (ProductID)
);

DROP TABLE PRODUCTS;

INSERT INTO CUSTOMERS(CUSTOMERID,FIRSTNAME,LASTNAME,ADDRESS,CITY,STATE,PHONENUMBER,EMAIL,AMAZONPRIME,DATEOFJOINING) VALUES(100,'John', 'Cena', '123 Ucantseeme St', 'West Newbury', 'Ma', '9825561020', 'jcena@wwe.com', 'Y', sysdate);
 
INSERT INTO CUSTOMERS(CUSTOMERID,FIRSTNAME,LASTNAME,ADDRESS,CITY,STATE,PHONENUMBER,EMAIL,AMAZONPRIME,DATEOFJOINING) VALUES(Customer_seq.nextval,'Timmy', 'Turner', '500 Wish Ave', 'Pixie', 'Tx', '8006772468', 'fairlyodd@gmail.com', 'N', sysdate);
 
INSERT INTO c(CUSTOMERID,FIRSTNAME,LASTNAME,ADDRESS,CITY,STATE,PHONENUMBER,EMAIL,AMAZONPRIME,DATEOFJOINING) VALUES(Customer_seq.nextval,'Santa', 'Clause', '1221 Red Nose St', 'North Pole', 'Wy', '3201155000', 'charcoal@hotmail.com', 'Y', sysdate);
 
INSERT INTO CUSTOMERS(CUSTOMERID,FIRSTNAME,LASTNAME,ADDRESS,CITY,STATE,PHONENUMBER,EMAIL,AMAZONPRIME,DATEOFJOINING) VALUES(Customer_seq.nextval,'Parker', 'Peter', '20 Ingram St', 'Queens', 'Ny', '2173652276', 'webslinger@yahoo.com', 'N', sysdate);
 
INSERT INTO CUSTOMERS(CUSTOMERID,FIRSTNAME,LASTNAME,ADDRESS,CITY,STATE,PHONENUMBER,EMAIL,AMAZONPRIME,DATEOFJOINING) VALUES(Customer_seq.nextval,'Porky', 'Pig', '420 Loony Dr', 'Orlando', 'Fl', '7568124912', 'thatsallfolks@outlook.com', 'N', sysdate);

delete from customers where CUSTOMERID = 104;


create synonym c for customers;

SELECT * FROM CUSTOMERS;

CREATE SYNONYM product_info FOR Products;

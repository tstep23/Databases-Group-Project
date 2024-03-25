-- Table: Schedule
CREATE TABLE schedule (
    ID INTEGER PRIMARY KEY,
    date INTEGER CHECK (length(date) = 4),
    start_time INTEGER CHECK (length(start_time) = 4),
    hours INTEGER CHECK (hours BETWEEN 1 AND 12),
    w_ID INTEGER,
    FOREIGN KEY (w_ID) REFERENCES workers(ID)
);

-- Table: Customer
CREATE TABLE customer (
    ID INTEGER PRIMARY KEY,
    email TEXT CHECK (email LIKE '%_@%.%'),
    name TEXT,
    points INTEGER CHECK (points >= 0)
);

-- Table: Workers 
CREATE TABLE workers (
    ID INTEGER PRIMARY KEY,
    name TEXT,
    phone_number INTEGER CHECK (length(phone_number) = 10),
    bank_number INTEGER CHECK (length(bank_number) BETWEEN 8 AND 12),
    type CHAR CHECK (type IN ('e', 'm')),
    wage DECIMAL CHECK ((type = 'e' AND wage >= 12 AND wage <= 25) OR (type = 'm' AND wage >= 15 AND wage <= 30))    
);

-- Table: Products 
CREATE TABLE products (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    count INTEGER CHECK (count >= 0 AND count <= 20),
    price DECIMAL
);

-- Table: Transaction 
CREATE TABLE transactions (
    ID INTEGER PRIMARY KEY,
    count INTEGER,
    money DECIMAL,
    date INTEGER CHECK (length(date) = 4),
    p_ID INTEGER,
    w_ID INTEGER,
    c_ID INTEGER,
    FOREIGN KEY (p_ID) REFERENCES products(ID),
    FOREIGN KEY (w_ID) REFERENCES workers(ID),
    FOREIGN KEY (c_ID) REFERENCES customer(ID)
);

CREATE TABLE parts (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Type TEXT,
    price DECIMAL
);
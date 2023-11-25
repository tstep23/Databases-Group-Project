-- Table: Schedule
CREATE TABLE schedule (
    ID INTEGER PRIMARY KEY,
    date INTEGER,
    start_time TIME,
    hours INTEGER CHECK (hours >= 1 AND hours <=12)
);

-- Table: Customer
CREATE TABLE customer (
    ID INTEGER PRIMARY KEY,
    Email VARCHAR(255) CHECK (REGEXP_LIKE(email, '^[a-zA-Z0-9._%+-]+@(gmail|yahoo|pobox)\.com$')),
    Name VARCHAR(255),
    points INTEGER DEFAULT 0
);

-- Table: Product_Sale
CREATE TABLE product_sale (
    p_ID INTEGER,
    t_ID INTEGER,
    FOREIGN KEY (p_ID) REFERENCES products(ID),
    FOREIGN KEY (t_ID) REFERENCES transaction(ID),
    PRIMARY KEY (p_ID, t_ID)
);

-- Table: Worker_Sale
CREATE TABLE worker_sale (
    w_ID INTEGER,
    t_ID INTEGER,
    FOREIGN KEY (w_ID) REFERENCES workers(ID),
    FOREIGN KEY (t_ID) REFERENCES transaction(ID),
    PRIMARY KEY (w_ID, t_ID)
);

-- Table: Order_History
CREATE TABLE order_history (
    c_ID INTEGER,
    t_ID INTEGER,
    FOREIGN KEY (c_ID) REFERENCES customer(ID),
    FOREIGN KEY (t_ID) REFERENCES transaction(ID),
    PRIMARY KEY (c_ID, t_ID)
);

-- Table: Workers 
CREATE TABLE Workers (
    ID INTEGER PRIMARY KEY,
    NAME VARCHAR(255),
    phone_number BIGINT CHECK (LENGTH(phone_number) = 10),
    bank_number BIGINT CHECK (LENGTH(bank_number) >= 8 AND LENGTH(bank_number) <= 12),
    wage DECIMAL CHECK ((type = 'e' AND wage >= 12 AND wage <= 25) OR (type = 'm' AND wage >= 15 AND wage <= 30)),
    type CHAR CHECK (type IN ('e', 'm'))
);

-- Table: Products 
CREATE TABLE products (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(255),
    count INTEGER CHECK (count >= 0 AND count <= 20),
    Price DECIMAL
);

-- Table: Transaction 
CREATE TABLE transaction (
    ID INTEGER PRIMARY KEY,
    count INTEGER,
    money DECIMAL,
    date INTEGER
);

-- Table: Shifts 
CREATE TABLE shifts (
    w_ID INTEGER,
    s_ID INTEGER,
    FOREIGN KEY (w_ID) REFERENCES workers(ID),
    FOREIGN KEY (s_ID) REFERENCES schedule(ID),
    PRIMARY KEY (w_ID, s_ID)
);
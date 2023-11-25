-- Table: Schedule
CREATE TABLE IF NOT EXISTS Schedule (
    ShiftID INTEGER PRIMARY KEY,
    Date DATE,
    StartTime TIME,
    Hours DECIMAL(5, 2)
);

-- Table: CustomersAccounts
CREATE TABLE IF NOT EXISTS CustomersAccounts (
    MemberID INTEGER PRIMARY KEY,
    Email VARCHAR(255),
    Name VARCHAR(255),
    Field4 INTEGER
);

-- Table: Sales
CREATE TABLE IF NOT EXISTS Sales (
    SaleNumber INTEGER PRIMARY KEY,
    Count INTEGER,
    Money DECIMAL(10, 2),
    Date INTEGER
);

-- Table: Workers
CREATE TABLE IF NOT EXISTS Workers (
    ID INTEGER PRIMARY KEY,
    NAME VARCHAR(255),
    BankNumber VARCHAR(20),
    Wage DECIMAL(10, 2),
    Type VARCHAR(50)
);

-- Table: products
CREATE TABLE IF NOT EXISTS products (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Count INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL
);

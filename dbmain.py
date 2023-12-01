import database

conn = database.connect_to_database('database_project.db')

# Function to set user input for date, start_time, and hours
def set_schedule():
    w_id = input("Enter worker ID: ")
    sdate = input("Enter date (MMDDYYYY): ")
    start_time = input("Enter start time (HHMM): ")
    hours = input("Enter hours: ")
    return {"date": sdate, "start_time": start_time, "hours": hours, "w_ID": w_id}

def set_customer():
    cid = input("Enter customer ID: ")
    email = input("Enter customer email: ")
    cname = input("Enter customer name: ")
    points = input("Enter customer points: ")
    return {"ID": cid, "email": email, "name": cname, "points": points}

def set_worker():
    # Thank you :) - Jacob Rogers
    wid = input("Enter worker ID: ")
    wname = input("Enter worker name: ")
    phone = input("Enter worker phone number (10 digits): ")
    bank = input("Enter worker bank number (8-12 digits): ")
    type = input("Enter worker type ('e' for employee or 'm' for manager): ")
    wage = input("Enter worker wage (12-25 for employee or 15-30 for manager): ")
    return {"ID": wid, "name": wname, "phone_number": phone, "bank_number": bank, "type": type, "wage": wage}

def set_product():
    pid = input("Enter product ID: ")
    pname = input("Enter product name: ")
    pcount = input("Enter product count(1-20): ")
    price = input("Enter the price of the product: ")
    return {"ID": pid, "Name": pname, "count": pcount, "price": price}

def set_transaction():
    tid = input("Enter transaction ID: ")
    tcount = input("Enter transaction count: ")
    money = input("Enter transaction amount: ")
    tdate = input("Enter transaction date (MMDDYYYY): ")
    return {"ID": tid, "count": tcount, "money": money, "date": tdate}

# Queries for requesting information from the database
def get_worker_id():
    wid = input("Enter worker ID: ")
    query = f"SELECT ID, name FROM workers WHERE ID = ?;"
    cursor = conn.cursor()
    cursor.execute(query, (wid,))
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Invalid worker ID, please try again.")
        return None
    else:
        return wid, rows[0][1]
    
def get_schedule(wid):
    query = f"SELECT date, start_time, hours FROM schedule WHERE w_ID = ?;"
    cursor = conn.cursor()
    cursor.execute(query, (wid,))
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No schedule found for this worker.")
    else:
        for row in rows:
            print("Date:", row[0])
            print("Start Time:", row[1])
            print("Hours:", row[2])
            
def get_wage(wid):
    query = f"SELECT wage FROM workers WHERE ID = ?;"
    cursor = conn.cursor()
    cursor.execute(query, (wid,))
    rows = cursor.fetchall()
    
    if len(rows) == 0:
        print("No wage found for this worker.")
    else:
        for row in rows:
            print("Wage:", row[0])

def get_customer_id(email):
    query = f"SELECT ID FROM customer WHERE email = ?;"
    cursor = conn.cursor()
    cursor.execute(query, (email,))
    row = cursor.fetchone()
    if row is not None:
        return row[0]
    else:
        return None

def get_transaction(c_ID):
    query = f"SELECT * FROM transaction WHERE c_ID = ?;"
    cursor = conn.cursor()
    cursor.execute(query, (c_ID,))
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No transactions found.")
    else:
        for row in rows:
            print("ID:", row[0])
            print("Count:", row[1])
            print("Money:", row[2])
            print("Date:", row[3])
            print()  # New line for each transaction

    
def get_product_id():
    pid = input("Enter product ID: ")
    query = f"SELECT * FROM products WHERE ID = ?;"
    cursor = conn.cursor()
    cursor.execute(query, (pid,))
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Invalid product ID, please try again.")
        return None
    else:
        return pid
    
def get_products():
    query = f"SELECT ID, Name, count, price FROM products;"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No products found.")
    else:
        for row in rows:
            print("ID:", row[0])
            print("Name:", row[1])
            print("Count:", row[2])
            print("Price:", row[3])
            print() # New line for each product

# Connect to the database
def managedb(cursor):
    while True:
        conn = database.connect_to_database('database_project.db')
        # Get user input for the table and operation
        table = input("\nEnter table name (schedule, customer, workers, products, transaction, CLOSE): ").lower()

        if table == "close":
            print("Closing")
            break  # Exit the loop and close the program

        if table not in ["schedule", "customer", "workers", "products", "transaction"]:
            print("Invalid table name. Enter valid table. ")
            continue

        # Get user input for the operation
        operation = input("Choose operation (ADD, DELETE, VIEW, UPDATE): ").upper()

        # Perform the selected operation
        if operation == "ADD":
            print(f"Enter values for the new entry in the '{table}' table:")
            if table == "schedule":
                data = set_schedule()
            elif table == "customer":
                data = set_customer()
            elif table == "workers":
                data = set_worker()
            elif table == "products":
                data = set_product()
            elif table == "transaction":
                data = set_transaction()

            # Construct the query dynamically using placeholders
            placeholders = ', '.join('?' for _ in data)
            columns = ', '.join(data.keys())
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders});"

            # Execute the query with the values
            cursor = conn.cursor()
            cursor.execute(query, tuple(data.values()))
            conn.commit()
            print("Data added successfully.")
        elif operation == "DELETE":
            entry_id = input(f"Enter ID of the entry to delete from the '{table}' table: ")
            query = f"DELETE FROM {table} WHERE ID = ?;"
            cursor = conn.cursor()
            cursor.execute(query, (entry_id,))
            conn.commit()
            print("Entry deleted successfully.")
        elif operation == "VIEW":
            print(f"All entries in the '{table}' table:")
            query = f"SELECT * FROM {table};"
            rows = cursor.execute(query)
            for row in rows:
                print(row)
        elif operation == "UPDATE":
            entry_id = input(f"Enter ID of the entry to update in the '{table}' table: ")
            print(f"Enter the updated details for the '{table}' table:")
            if table == "schedule":
                data = set_schedule()
            elif table == "customer":
                data = set_customer()
            elif table == "workers":
                data = set_worker()
            elif table == "products":
                data = set_product()
            elif table == "transaction":
                data = set_transaction()

            # Construct the SET clause dynamically using placeholders
            set_clause = ', '.join(f"{key} = ?" for key in data.keys())
            query = f"UPDATE {table} SET {set_clause} WHERE ID = ?;"

            # Execute the query with the values
            cursor = conn.cursor()
            cursor.execute(query, tuple(data.values()) + (entry_id,))
            conn.commit()
            print("Entry updated successfully.")
        else:
            print("Invalid operation. Please enter ADD, DELETE, VIEW, UPDATE, or CLOSE.")

    # Close the connection when done
    database.close_connection(conn)
    
def custom_query(conn):
    # Get user input for the query
    query = input("Enter query (e.g., SELECT * FROM workers): ")
    
    # Execute the query
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Print the results
        if len(rows) == 0:
            print("No results found.")
        else:
            for row in rows:
                print(row)
                
    except Exception as e:
        print("Error executing the query:", e)
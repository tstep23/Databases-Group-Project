import database

# Function to get user input for date, start_time, and hours
def get_schedule_input():
    sdate = input("Enter date (MMDDYYYY): ")
    start_time = input("Enter start time (HHMM): ")
    hours = input("Enter hours: ")
    return {"date": sdate, "start_time": start_time, "hours": hours}

def get_customer_input():
    cid = input("Enter customer ID: ")
    email = input("Enter customer email: ")
    cname = input("Enter customer name: ")
    points = input("Enter customer points: ")
    return {"ID": cid, "email": email, "name": cname, "points": points}

def get_workers_input():
    wid = input("Enter worker ID: ")
    wname = input("Enter worker name: ")
    phone = input("Enter worker phone number (10 digits): ")
    bank = input("Enter worker bank number (8-12 digits): ")
    type = input("Enter worker type ('e' for employee or 'm' for manager): ")
    wage = input("Enter worker wage (12-25 for employee or 15-30 for manager): ")
    return {"ID": wid, "name": wname, "phone_number": phone, "bank_number": bank, "type": type, "wage": wage}

def get_products_input():
    pid = input("Enter product ID: ")
    pname = input("Enter product name: ")
    pcount = input("Enter product count(1-20): ")
    price = input("Enter the price of the product: ")
    return {"ID": pid, "Name": pname, "count": pcount, "price": price}

def get_transaction_input():
    tid = input("Enter transaction ID: ")
    tcount = input("Enter transaction count: ")
    money = input("Enter transaction amount: ")
    tdate = input("Enter transaction date (MMDDYYYY): ")
    return {"ID": tid, "count": tcount, "money": money, "date": tdate}

# Connect to the database
conn = database.connect_to_database('database_project.db')

while True:
    # Get user input for the table and operation
    table = input("Enter table name (schedule, customer, workers, products, transaction, CLOSE): ").lower()

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
            data = get_schedule_input()
        elif table == "customer":
            data = get_customer_input()
        elif table == "workers":
            data = get_workers_input()
        elif table == "products":
            data = get_products_input()
        elif table == "transaction":
            data = get_transaction_input()

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
            data = get_schedule_input()
        elif table == "customer":
            data = get_customer_input()
        elif table == "workers":
            data = get_workers_input()
        elif table == "products":
            data = get_products_input()
        elif table == "transaction":
            data = get_transaction_input()

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
import sqlite3
import dbmain

def connect_to_database(database_project):
    return sqlite3.connect(database_project)

def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def fetch_data(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def close_connection(conn):
    conn.close()
    
def worker_menu(conn, cursor):
    while True:
        print("\nEnter employee type: ")
        print("1. Employee")
        print("2. Manager")
        print("3. Exit")
        worker_choice = input("Enter your choice: ")
        
        if worker_choice == "1":
            wid = dbmain.get_worker_id()
            while wid is not None:
                print("\nEmployee Menu for ID " + wid + ":")
                print("1. View Schedule")
                print("2. View Products")
                print("3. View Wage")
                print("4. Exit")
                employee_choice = input("Enter your choice: ")
                
                if employee_choice == "1":
                    # Call function to display schedule
                    dbmain.get_schedule_input()
                elif employee_choice == "2":
                    # Call function to display products
                    dbmain.get_products_input()
                elif employee_choice == "3":
                    dbmain.get_wage_input() # TODO: Implement this function
                elif employee_choice == "4":
                    break
                else:
                    print("Invalid input, please try again.")
            
        elif worker_choice == "2":
            print("\nManager Menu:")
            print("1. View Schedule")
            print("2. View Products")
            print("3. View Wage")
            print("4. Manage Database")
            print("5. Exit")
            employee_choice = input("Enter your choice: ")
            
            if employee_choice == "1":
                # Call function to display schedule
                dbmain.get_schedule_input()
            elif employee_choice == "2":
                # Call function to display products
                dbmain.get_products_input()
            elif employee_choice == "3":
                dbmain.get_wage_input() # TODO: Implement this function
            elif employee_choice == "4":
                # Call function to manage employees
                dbmain.managedb(cursor)
            else:
                print("Invalid input, please try again.")
        elif worker_choice == "3":
            break
        else:
            print("Invalid input, please try again.")
        
            
def customer_menu(conn):
    while True:
        print("\nCustomer Menu:")
        print("1. View Products")
        print("2. View Transactions")
        print("3. Exit")
        
        customer_choice = input("Enter your choice: ")
        
        if customer_choice == "1":
            # Call function to display products
            dbmain.get_products_input()
        elif customer_choice == "2":
            # Call function to display schedule
            dbmain.get_transaction_input()
        elif customer_choice == "3":
            break
        else:
            print("Invalid input, please try again.")        
            
def main():
    # Connect to database
    conn = connect_to_database("database_project.db")
    cursor = conn.cursor()

    while True:
        print("\nWelcome to the database project!")
        print("1. Worker")
        print("2. Customer")
        print("3. Exit")
        
        role_choice = input("Enter your role: ")
        
        if role_choice == "1":
            # Call function to display worker menu
            worker_menu(conn, cursor)
        elif role_choice == "2":
            # Call function to display customer menu
            customer_menu(conn)
        elif role_choice == "3":
            break
        else:
            print("Invalid input, please try again.")
        
    # Close connection to database
    close_connection(conn)
    
if __name__ == "__main__":
    main()
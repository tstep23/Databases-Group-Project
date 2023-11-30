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
    
def worker_menu(conn):
    while True:
        print("Enter employee type: ")
        print("1. Employee")
        print("2. Manager")
        print("3. Exit")
        worker_choice = input("Enter your choice: ")
        
        if worker_choice == "1":
            print("Employee Menu:")
            print("1. View Schedule")
            print("2. View Products")
            print("3. View Wage")
            print("3. Exit")
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
            print("Manager Menu:")
            print("1. View Schedule")
            print("2. View Products")
            print("3. View Wage")
            print("3. Exit")
            employee_choice = input("Enter your choice: ")
            
            if employee_choice == "1":
                # Call function to display schedule
                dbmain.get_schedule_input()
            elif employee_choice == "2":
                # Call function to display products
                dbmain.get_products_input()
            elif employee_choice == "3":
                dbmain.get_wage_input() # TODO: Implement this function
            else:
                print("Invalid input, please try again.")
        elif worker_choice == "3":
            break
        else:
            print("Invalid input, please try again.")
        
            
def customer_menu(conn):
    while True:
        print("Customer Menu:")
        print("1. View Products")
        print("2. View Transactions")
        print("3. Exit")
        
        customer_choice = input("Enter your choice: ")
        
        if customer_choice == "1":
            # Call function to display products
            dbmain.get_products_input()
        elif customer_choice == "2":
            # Call function to display schedule
            dbmain.get_schedule_input()
        elif customer_choice == "3":
            break
        else:
            print("Invalid input, please try again.")

def manager_menu(conn):
    while True:
        print("Administrator Menu:")
        print("1. Manage Database")
        print("2. Exit")
    
        manager_choice = input("Enter your choice: ")
        
        if manager_choice == "1":
            # Call function to display database menu
            dbmain.managedb()
        elif manager_choice == "2":
            break
        else:
            print("Invalid input, please try again.")            
            
            
def main():
    # Connect to database
    conn = connect_to_database("database_project.db")
    
    while True:
        print("Welcome to the database project!")
        print("1. Worker")
        print("2. Customer")
        print("3. Administrator")
        print("4. Exit")
        
        role_choice = input("Enter your choice: ")
        
        if role_choice == "1":
            # Call function to display worker menu
            worker_menu(conn)
        elif role_choice == "2":
            # Call function to display customer menu
            customer_menu(conn)
        elif role_choice == "3":
            # Call function to display manager menu
            manager_menu(conn)
        elif role_choice == "4":
            break
        else:
            print("Invalid input, please try again.")
        
    # Close connection to database
    close_connection(conn)
    
if __name__ == "__main__":
    main()
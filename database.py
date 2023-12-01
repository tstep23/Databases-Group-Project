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
            worker_info = dbmain.get_worker_id()
            while worker_info is not None:
                wid, name = worker_info
                print("\nEmployee Menu for " + name + ":")
                print("1. View Schedule")
                print("2. View Products")
                print("3. View Wage")
                print("4. Exit")
                employee_choice = input("Enter your choice: ")
                
                if employee_choice == "1":
                    # Call function to display schedule
                    dbmain.get_schedule(wid)
                elif employee_choice == "2":
                    # Call function to display products
                    dbmain.get_products()
                elif employee_choice == "3":
                    dbmain.get_wage(wid) # 
                elif employee_choice == "4":
                    break
                else:
                    print("Invalid input, please try again.")
            
        elif worker_choice == "2":
            worker_info = dbmain.get_worker_id()
            while worker_info is not None:
                wid, name = worker_info
                print("\nManager Menu for " + name + ":")
                print("1. View Schedule")
                print("2. View Products")
                print("3. View Wage")
                print("4. Manage Database")
                print("5. Exit")
                employee_choice = input("Enter your choice: ")
                
                if employee_choice == "1":
                    # Call function to display schedule
                    dbmain.get_schedule(wid)
                elif employee_choice == "2":
                    # Call function to display products
                    dbmain.get_products()
                elif employee_choice == "3":
                    dbmain.get_wage(wid)
                elif employee_choice == "4":
                    # Call function to manage employees
                    dbmain.managedb(cursor)
                elif employee_choice == "5":
                    break
                else:
                    print("Invalid input, please try again.")
        elif worker_choice == "3":
            break
        else:
            print("Invalid input, please try again.")
        
            
def customer_menu(conn):
    while True:
        print("Enter customer email: ")
        email = input()
        
        c_ID = dbmain.get_customer_id(email)
        
        if c_ID is not None:
            print("\nCustomer Menu for " + email + ":")
            print("1. View Products")
            print("2. View Transactions")
            print("3. Exit")
            
            customer_choice = input("Enter your choice: ")
            
            if customer_choice == "1":
                # Call function to display products
                dbmain.get_products()
            elif customer_choice == "2":
                # Call function to display transactions
                dbmain.get_transaction(c_ID)
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
        print("3. Custom Query")
        print("4. Exit")
        
        role_choice = input("Enter your role: ")
        
        if role_choice == "1":
            # Call function to display worker menu
            worker_menu(conn, cursor)
        elif role_choice == "2":
            # Call function to display customer menu
            customer_menu(conn)
        elif role_choice == "3":
            # Call function to display custom query menu
            dbmain.custom_query(conn)
        elif role_choice == "4":
            break
        else:
            print("Invalid input, please try again.")
        
    # Close connection to database
    close_connection(conn)
    
if __name__ == "__main__":
    main()
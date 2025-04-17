import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="mydatabase",
        user="postgres",
        password="123456789"
    )

def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARCHAR(20)
        );
    """)

def insert_csv(cursor):
    file_path = input("Enter CSV path: ")
    try:
        with open(file_path, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    cursor.execute(
                        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                        (row[0], row[1])
                    )
                except Exception as e:
                    print(f"Error inserting {row}: {e}")
    except FileNotFoundError:
        print("CSV file not found.")

def insert_console(cursor):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cursor.execute(
            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
            (name, phone)
        )
    except Exception as e:
        print(f"Error: {e}")

def update_user(cursor):
    method = input("Update by (phone or name)? ").strip().lower()
    if method == "phone":
        phone = input("Enter existing phone: ")
        new_name = input("New name: ")
        cursor.execute(
            "UPDATE phonebook SET name = %s WHERE phone = %s",
            (new_name, phone)
        )
    elif method == "name":
        name = input("Enter existing name: ")
        new_phone = input("New phone: ")
        cursor.execute(
            "UPDATE phonebook SET phone = %s WHERE name = %s",
            (new_phone, name)
        )

def query_data(cursor):
    keyword = input("Search for name or phone: ")
    cursor.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s",
        (f"%{keyword}%", f"%{keyword}%")
    )
    for row in cursor.fetchall():
        print(row)

def delete_user(cursor):
    method = input("Delete by (name or phone)? ").strip().lower()
    if method == "name":
        name = input("Enter name to delete: ")
        cursor.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    elif method == "phone":
        phone = input("Enter phone to delete: ")
        cursor.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

def main():
    conn = connect()
    cur = conn.cursor()
    create_table(cur)
    conn.commit()

    while True:
        print("\n1. Insert from CSV")
        print("2. Insert from Console")
        print("3. Update User")
        print("4. Query Data")
        print("5. Delete User")
        print("6. Exit")
        choice = input("Choose an action: ").strip()

        if choice == "1":
            insert_csv(cur)
            conn.commit()
        elif choice == "2":
            insert_console(cur)
            conn.commit()
        elif choice == "3":
            update_user(cur)
            conn.commit()
        elif choice == "4":
            query_data(cur)
        elif choice == "5":
            delete_user(cur)
            conn.commit()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

    cur.close()
    conn.close()
main()
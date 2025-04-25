import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="phonebook1",
        user="postgres",
        password="123456789",
        host="localhost",
        client_encoding='UTF8'
    )

def collecting_info_by_pattern(pattern):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT name, phone FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", 
                            ('%' + pattern + '%', '%' + pattern + '%'))
                rows = cur.fetchall()
                if not rows:
                    print("No records matching the query.")
                else:
                    print("Number of found records: ", cur.rowcount)
                    for row in rows:
                        print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def insert_or_update_user(name, phone):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM phonebook WHERE name = %s", (name,))
                count = cur.fetchone()[0]

                if count > 0:
                    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
                else:
                    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))

                conn.commit()
                print(f"Contact {name} successfully added or updated.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")                  

def collecting_info_with_pagination(limit, offset):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id, name, phone FROM phonebook ORDER BY user_id LIMIT %s OFFSET %s", (limit, offset))
                rows = cur.fetchall()
                if not rows:
                    print("No records on this page.")
                else:
                    print("Number of found records: ", cur.rowcount)
                    for row in rows:
                        print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def delete_user_by_name(name):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
                conn.commit()
                print(f"Contact with name {name} successfully deleted.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def delete_user_by_phone(phone):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
                conn.commit()
                print(f"Contact with phone number {phone} successfully deleted.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

if __name__ == '__main__':
    while True:
        operation = input("Choose operation:\n1 - Add contact\n2 - Update contact\n3 - Search contacts\n4 - Delete contact\n5 - Add multiple contacts\n6 - Quit:\n")

        if operation == "1":
            name = input("Enter new contact name: ")
            phone = input("Enter new contact phone number: ")
            insert_or_update_user(name, phone)

        elif operation == "2":
            name = input("Enter contact name to update: ")
            phone = input("Enter new phone number: ")
            insert_or_update_user(name, phone)

        elif operation == "3":
            pattern = input("Enter pattern (part of name, surname, or phone number): ")
            collecting_info_by_pattern(pattern)

        elif operation == "4":
            delete_type = input("Delete by:\n1 - Name\n2 - Phone number\nChoose type: ")
            if delete_type == "1":
                name = input("Enter contact name to delete: ")
                delete_user_by_name(name)
            elif delete_type == "2":
                phone = input("Enter phone number to delete: ")
                delete_user_by_phone(phone)

        elif operation == "5":
            num_contacts = int(input("Enter number of contacts to add: "))
            for _ in range(num_contacts):
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                insert_or_update_user(name, phone)
        elif operation == "6":
            break

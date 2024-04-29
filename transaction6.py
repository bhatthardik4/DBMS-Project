import psycopg2

def display_data(cursor, tables):
    for table, condition in tables:
        cursor.execute(f"SELECT * FROM {table};")
        print(f"Data from {table}:")
        for row in cursor.fetchall():
            print(row)
            print("\n")

def run_transaction(conn_params):
    with psycopg2.connect(**conn_params) as conn:
        conn.autocommit = False
        with conn.cursor() as cursor:
            # Display data before transaction
            print("Before Transaction:")
            display_data(cursor, [("stock", "depid = 'd1'"), ("depot", "depid = 'd1'")])

            # Execute transaction
            cursor.execute("""
                BEGIN;
                INSERT INTO Depot(depid, addr, volume) VALUES (%s, %s, %s);
                INSERT INTO Stock(prodid, depid, quantity) VALUES (%s, %s, %s);
                COMMIT;
            """, ('d100', 'Chicago', 100, 'pp1', 'd100', 100))

            #print output message
            print("\n--------------------------------------------------------")
            print("New Depot D100 Added in Stock and Depot")
            print("--------------------------------------------------------\n")

            # Display data after transaction
            print("After Transaction:")
            display_data(cursor, [("stock", "depid = 'd1'"), ("depot", "depid = 'd1'")])

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
            display_data(cursor, [("stock", "prodid = 'p1'"), ("product", "prodid = 'p1'")])

            # Execute transaction
            cursor.execute("""
                BEGIN;
                INSERT INTO Product(prodid, pname, price) VALUES (%s, %s, %s);
                INSERT INTO Stock(prodid, depid, quantity) VALUES (%s, %s, %s);
                COMMIT;
            """, ('p100', 'cd', 5, 'p100', 'd2', 50))

            #print output message
            print("\n--------------------------------------------------------")
            print("New Product p100 added in Stock and Product")
            print("--------------------------------------------------------\n")

            # Display data after transaction
            print("After Transaction:")
            display_data(cursor, [("stock", "prodid = 'pp1'"), ("product", "prodid = 'pp1'")])

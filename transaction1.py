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
            display_data(cursor, [("Product", "prodid = 'p1'"), ("Stock", "prodid = 'p1'")])

            # Execute transaction
            cursor.execute("""
                BEGIN;
                DELETE FROM Product WHERE prodid = 'p1';
                COMMIT;
            """)

            #print output message
            print("\n--------------------------------------------------------")
            print("Data Deleted from Product and Stock whose id was p1")
            print("--------------------------------------------------------\n")

            # Display data after transaction
            print("After Transaction:")
            display_data(cursor, [("Product", "prodid = 'p1'"), ("Stock", "prodid = 'p1'")])

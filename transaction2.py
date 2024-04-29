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
            display_data(cursor, [("Depot", "depid = 'p1'"), ("Stock", "depid = 'p1'")])

            # Execute transaction
            cursor.execute("""
                BEGIN;
                DELETE FROM Depot WHERE depid = 'd1';
                COMMIT;
            """)

            #print output message
            print("\n--------------------------------------------------------")
            print("Data Deleted from Depot and Stock whose DepotID was D1")
            print("--------------------------------------------------------\n")

            # Display data after transaction
            print("After Transaction:")
            display_data(cursor, [("Depot", "depid = 'p1'"), ("Stock", "depid = 'p1'")])

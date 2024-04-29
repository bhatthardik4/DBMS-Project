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
                UPDATE Depot SET depid = 'dd1' WHERE depid = 'd1';
            """, ('dd1', 'd1', 'dd1', 'd1'))

            #print output message
            print("\n--------------------------------------------------------")
            print("D1 name Changed to DD1 in Depot and Stock")
            print("--------------------------------------------------------\n")

            # Display data after transaction
            print("After Transaction:")
            display_data(cursor, [("stock", "depid = 'd1'"), ("depot", "depid = 'd1'")])

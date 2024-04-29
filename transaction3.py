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
            # Begin transaction
            cursor.execute("BEGIN;")

            cursor.execute(""" TRUNCATE TABLE Stock, Product, Depot; """)

            # Insert data into Product
            cursor.execute("""
                                            INSERT INTO Product (prodid, pname, price) VALUES
                                            ('p1', 'tape', 2.5),
                                            ('p2', 'tv', 250),
                                            ('p3', 'vcr', 80);
                                        """)

            # Insert data into Depot
            cursor.execute("""
                                            INSERT INTO Depot (depid, addr, volume) VALUES
                                            ('d1', 'newyork', 9000),
                                            ('d2', 'sycrause', 6000),
                                            ('d4', 'newyork', 2000);
                                        """)

            # Insert data into Stock
            cursor.execute("""
                                            INSERT INTO Stock (prodid, depid, quantity) VALUES
                                            ('p1', 'd1', 1000),
                                            ('p1', 'd2', -100),
                                            ('p1', 'd4', 1200),
                                            ('p3', 'd1', 3000),
                                            ('p3', 'd4', 2000),
                                            ('p2', 'd4', 1500),
                                            ('p2', 'd1', -400),
                                            ('p2', 'd2', 2000);
                                        """)

            # Commit the transaction
            cursor.execute("COMMIT;")

            print("Before Transaction:")
            display_data(cursor, [("stock", "prodid = 'p1'"), ("product", "prodid = 'p1'")])

            cursor.execute("BEGIN;")

            # Update prodid in Stock table
            cursor.execute("UPDATE Product SET prodid = 'pp1' WHERE prodid = 'p1';")

            # Commit the transaction
            cursor.execute("COMMIT;")

            #print output message
            print("\n--------------------------------------------------------")
            print("P1 ID Changed to PP1 in Stock and Product")
            print("--------------------------------------------------------\n")

            # Display data after transaction
            print("After Transaction:")
            display_data(cursor, [("stock", "prodid = 'p1'"), ("product", "prodid = 'p1'")])

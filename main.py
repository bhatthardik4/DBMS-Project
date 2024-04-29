import importlib
import importlib.util
import os
import psycopg2

conn_params = {
    'dbname': 'karandavda',
    'user': 'karandavda',
    'password': 'KaranDavda@1719',
    'host': 'localhost',
    'port': '5432'
}

def list_transactions():
    print("Available Transactions:")
    transactions = [f"T{file[11]}" for file in os.listdir("transactions") if file.startswith("transaction")]
    for transaction in transactions:
        print(f"- {transaction}")
    return transactions

def execute_transaction(transaction_name):
    module = importlib.import_module(f"transactions.{transaction_name}")
    module.run_transaction(conn_params)


def main():
    try:
            with psycopg2.connect(**conn_params) as conn:
                conn.autocommit = False  # Turn off autocommit

            while True:
                print("\nAvailable Transactions:")
                print("1. Delete product p1 from Product and Stock")
                print("2. Delete depot d1 from Depot and Stock")
                print("3. Change product p1's ID to pp1 in Product and Stock")
                print("4. Change depot d1's name to dd1 in Depot and Stock")
                print("5. Add product P100 in Product and P100 in Stock")
                print("6. Add depot D100 in Depot and D100 in Stock")
                print("0. Exit")

                choice = input("\nEnter transaction number to execute (0 to exit): ")
                if choice == '0':
                    break

                transaction_file = f"transaction{choice}.py"
                spec = importlib.util.spec_from_file_location("transaction_module", transaction_file)
                transaction_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(transaction_module)

                # Execute the transaction function
                transaction_module.run_transaction(conn_params)

            print("All transactions completed successfully.")

    except Exception as e:
        print("An error occurred:", e)


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
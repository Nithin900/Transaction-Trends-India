import pandas as pd
import sqlite3

def create_table():
 # make a connection to the SQLite database -open connection
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()   

    # Create a table in the database
    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        date DATE,
        card_type TEXT,
        exp_type TEXT,
        gender TEXT,
        amount INTEGER);
    ''')


    # Close the connection
    conn.close()

def insert_data():
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(r'Credit card transactions_India_Simple.csv')

    # Establish a connection to the SQLite database
    conn = sqlite3.connect('transactions.db')

    # Insert data from the DataFrame into the database
    df.to_sql('transactions', conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()

def get_data():
    # Establish a connection to the SQLite database
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()

    # Execute the SELECT query
    c.execute('''SELECT * FROM transactions''')

    # Fetch all rows from the result set
    rows = c.fetchall()
    # Print the data
    for row in rows:
        print(row)
    # Close the connection
    conn.close()

    # Convert SQLite data to Pandas DataFrame
    df = pd.DataFrame(rows, columns=[col[0] for col in c.description])

    return df

if __name__ == '__main__':
    create_table()
    insert_data()

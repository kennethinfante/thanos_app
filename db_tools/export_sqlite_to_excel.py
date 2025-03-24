import sqlite3
import pandas as pd
import os

def export_sqlite_to_excel(db_path, excel_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # Get a list of all tables in the database
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Create a Pandas Excel writer using XlsxWriter as the engine
    with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
        for table in tables:
            table_name = table[0]
            # Read the table into a pandas DataFrame
            df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
            
            # Write the DataFrame to an Excel sheet
            df.to_excel(writer, sheet_name=table_name, index=False)

            print(f"Exported table: {table_name}")

    # Close the database connection
    conn.close()

    print(f"All tables exported to {excel_path}")

if __name__ == "__main__":
    # Specify the path to your SQLite database
    db_path = "../acctg.db"
    
    # Specify the path for the output Excel file
    excel_path = "acctg_export.xlsx"
    
    export_sqlite_to_excel(db_path, excel_path)
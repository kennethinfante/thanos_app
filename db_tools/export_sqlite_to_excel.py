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
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        for table in tables:
            table_name = table[0]
            # Read the table into a pandas DataFrame
            df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

            for col in ['date', 'due_date']:
                try:
                    # Convert to datetime and then format to yyyy-mm-dd
                    temp_dates = pd.to_datetime(df[col], errors='coerce')
                    # Only update the column if conversion was successful
                    if not temp_dates.isna().all():
                        df[col] = temp_dates.dt.strftime('%Y-%m-%d')
                except:
                    # Silently skip columns that can't be formatted as dates
                    pass

            # Write the DataFrame to an Excel sheet
            df.to_excel(writer, sheet_name=table_name, index=False)

            print(f"Exported table: {table_name}")

    # Close the database connection
    conn.close()

    print(f"All tables exported to {excel_path}")

if __name__ == "__main__":
    # Specify the path to your SQLite database
    db_path = "acctg_db4/accounting.db"
    
    # Specify the path for the output Excel file
    excel_path = "acctg_db4/acctg_export4.xlsx"
    
    export_sqlite_to_excel(db_path, excel_path)
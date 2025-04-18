import pandas as pd
import sqlite3
import os
import argparse
from fks import *

def get_create_query(sheet_name, columns):
    create_query = f"CREATE TABLE IF NOT EXISTS {sheet_name} (\nid INTEGER"

    # create_query += ",\n".join([f"{col} TEXT" for col in columns if col != 'id'])
    for col in columns:
        if col == 'id':
            continue
        elif col.endswith("_id"):
            create_query += f",\n{col} INTEGER"
        elif col.endswith("_amount") or \
            col.endswith("_balance") or \
            col.endswith("_price") or \
            col in ("debit", "credit") or \
            col == "amount":
            create_query += f",\n{col} DECIMAL(15,2) DEFAULT 0"
        elif col.endswith("_number") or \
            col in ("sku", "code"):
            create_query += f",\n{col} TEXT NOT NULL UNIQUE"
        elif col == "created_at":
            create_query += f",\n{col} TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
        elif sheet_name == "bills" and col == "status":
            create_query += f",\n{col} TEXT DEFAULT 'draft', -- draft, received, paid, partially_paid, overdue, cancelled"
        elif sheet_name == "invoices" and col == "status":
            create_query += f",\n{col} TEXT DEFAULT 'draft', -- draft, sent, paid, partially_paid, overdue, cancelled"
        elif col in ("is_posted", "is_reconciled", "is_closed", "is_default"):
            create_query += f",\n{col} BOOLEAN DEFAULT 0"
        elif col in ("is_active"):
            create_query += f",\n{col} BOOLEAN DEFAULT 1"
        else:
            create_query += f",\n{col} TEXT"
            
    create_query += ",\nPRIMARY KEY ('id' AUTOINCREMENT)\n);"

    return create_query

def get_insert_query(sheet_name, df):
    values = ""

    columns = ', '.join(df.columns.tolist())
    
    for _, row in df.iterrows():
        value_list = []
        for value in row:

            str_value = str(value).rstrip()

            # don't worry for now of fk becoming float, they work the same as integer in sqlite
            if str_value.replace('.','').isdigit():
                value_list.append(str_value)
            elif pd.notna(value):
                value_list.append(f'"{str_value}"')
            else:
                value_list.append('NULL')
        
        values += "\n(" + ', '.join(value_list) + "),"
        # values += "\n(" + ', '.join([f'"{str(value)}"' if pd.notna(value) else 'NULL' for value in row]) + "),"

    values.rstrip(',')

    return f"INSERT INTO {sheet_name} ({columns}) VALUES ({values}\n);"

def add_foreign_keys(table_queries, fks):
    for sheet_name, fks in fks.items():
        create_query = table_queries[sheet_name]
        create_query = create_query.replace("\n);", "")
        for fk in fks:
            create_query += f",\nFOREIGN KEY ({fk[0]}) REFERENCES {fk[1]}({fk[2]})"
        create_query += "\n);"
        
        table_queries[sheet_name] = create_query

    return table_queries

def import_excel_to_sqlite(fks, excel_path, sql_output_path, db_path):
    # Delete the existing database file if it exists
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
            print(f"Existing database file deleted: {db_path}")
        except Exception as e:
            print(f"Warning: Could not delete existing database file: {e}")

    # Read the Excel file
    xls = pd.ExcelFile(excel_path, engine="openpyxl")

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Dictionary to store table creation queries
    table_queries = {}

    sql_file = open(sql_output_path, 'w')

    # First pass: Create tables without foreign key constraints
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        columns = df.columns.tolist()
        
        create_query = get_create_query(sheet_name, columns)
        
        table_queries[sheet_name] = create_query

    # Second pass: Add foreign key constraints
    table_queries = add_foreign_keys(table_queries, fks)
    
    # separate exece because the fk dict above may not include all the tables in the excel file
    for sheet_name, create_query in table_queries.items():
        print(create_query)
        cursor.execute(create_query)
        sql_file.write(f"{create_query}\n\n")

    # Insert data into tables
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        df.to_sql(sheet_name, conn, if_exists='replace', index=False)
        # conn.execute(f'ALTER TABLE {sheet_name} ADD PRIMARY KEY (id);')

        # Generate and write INSERT statements
        insert_query = get_insert_query(sheet_name, df)

        sql_file.write(f"{insert_query}\n\n")

    # Commit changes and close connection
    conn.commit()
    conn.close()
    sql_file.close()

    print(f"Excel file imported to SQLite database: {db_path} with {len(table_queries)} tables.")
    print(f"SQL statements exported to: {sql_output_path}")

if __name__ == "__main__":
    
    import_excel_to_sqlite(fk5, **acctg_set5)
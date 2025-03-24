import pandas as pd
import sqlite3
import os

def import_excel_to_sqlite(excel_path, db_path):
    # Read the Excel file
    xls = pd.ExcelFile(excel_path)

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Dictionary to store table creation queries
    table_queries = {}

    # First pass: Create tables without foreign key constraints
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        columns = df.columns.tolist()
        
        create_query = f"CREATE TABLE IF NOT EXISTS {sheet_name} (\n"
        create_query += "id INTEGER PRIMARY KEY"
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
        # create_query += ",\n".join([f"{col} TEXT" for col in columns if col != 'id'])
        create_query += "\n);"
        
        table_queries[sheet_name] = create_query
        # cursor.execute(create_query)

    # Second pass: Add foreign key constraints
    foreign_keys = {
        'accounts': [('account_type_id', 'account_types', 'id'), ('parent_account_id', 'accounts', 'id')],
        'contacts': [('type_id', 'contact_types', 'id')],
        'bank_accounts': [('account_id', 'accounts', 'id'), ('currency_id', 'currencies', 'id')],
        'journal_entry_lines': [('journal_entry_id', 'journal_entries', 'id'), ('account_id', 'accounts', 'id')],
        'products': [('category_id', 'product_categories', 'id'), ('tax_rate_id', 'tax_rates', 'id'),
                     ('inventory_account_id', 'accounts', 'id'), ('revenue_account_id', 'accounts', 'id'),
                     ('expense_account_id', 'accounts', 'id')],
        'invoices': [('customer_id', 'contacts', 'id')],
        'invoice_lines': [('invoice_id', 'invoices', 'id'), ('product_id', 'products', 'id'),
                          ('tax_rate_id', 'tax_rates', 'id')],
        'bills': [('vendor_id', 'contacts', 'id')],
        'bill_lines': [('bill_id', 'bills', 'id'), ('product_id', 'products', 'id'),
                       ('tax_rate_id', 'tax_rates', 'id')],
        'invoice_payments': [('payment_method_id', 'payment_methods', 'id'), ('invoice_id', 'invoices', 'id')],
        'bill_payments': [('payment_method_id', 'payment_methods', 'id'), ('bill_id', 'bills', 'id')],
        'bank_transactions': [('bank_account_id', 'bank_accounts', 'id'), ('journal_entry_id', 'journal_entries', 'id'),
                              ('invoice_payment_id', 'invoice_payments', 'id'), ('bill_payment_id', 'bill_payments', 'id')]
    }

    # full support for alter table is not available in SQLite, so we'll simulate it
    # for table, fks in foreign_keys.items():
    #     print(table)
    #     print(fks)
    #     alter_query = f"ALTER TABLE {table}\n"
    #     for fk in fks:
    #         if fk == fks[-1]:
    #             alter_query += f"ADD CONSTRAINT fk_{table}_{fk[0]} FOREIGN KEY ({fk[0]}) REFERENCES {fk[1]}({fk[2]});\n"
    #         else:
    #             alter_query += f"ADD CONSTRAINT fk_{table}_{fk[0]} FOREIGN KEY ({fk[0]}) REFERENCES {fk[1]}({fk[2]}),\n"
    #     cursor.execute(alter_query)

    for table, fks in foreign_keys.items():
        create_query = table_queries[table]
        create_query = create_query.replace("\n);", ',\n')
        for fk in fks:
            if fk == fks[-1]:
                create_query += f"FOREIGN KEY ({fk[0]}) REFERENCES {fk[1]}({fk[2]})\n"
            else:
                create_query += f"FOREIGN KEY ({fk[0]}) REFERENCES {fk[1]}({fk[2]}),\n"
        create_query += ");"
        print(create_query)
        cursor.execute(create_query)

    # Insert data into tables
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        df.to_sql(sheet_name, conn, if_exists='replace', index=False)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"Excel file imported to SQLite database: {db_path}")

if __name__ == "__main__":
    # Specify the path to your Excel file
    excel_path = "acctg_export.xlsx"
    
    # Specify the path for the output SQLite database
    db_path = "../accounting.db"
    
    import_excel_to_sqlite(excel_path, db_path)
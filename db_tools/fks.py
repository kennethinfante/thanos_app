acctg_set1 = {
    "excel_path" : "acctg_db1/acctg_export1.xlsx", 
    "sql_output_path" : "acctg_db1/accounting.sql", 
    "db_path" : "acctg_db1/accounting.db"
}

fk1 = {
    'accounts': [('account_type_id', 'account_types', 'id'), ('parent_account_id', 'accounts', 'id')],
    'entities': [('type_id', 'entity_types', 'id')],
    'bank_accounts': [('account_id', 'accounts', 'id'), ('currency_id', 'currencies', 'id')],
    'journal_lines': [('journal_id', 'journals', 'id'), ('account_id', 'accounts', 'id')],
    'products': [('category_id', 'product_categories', 'id'), ('tax_rate_id', 'tax_rates', 'id'),
                    ('inventory_account_id', 'accounts', 'id'), ('revenue_account_id', 'accounts', 'id'),
                    ('expense_account_id', 'accounts', 'id')],
    'invoices': [('customer_id', 'entities', 'id')],
    'invoice_lines': [('invoice_id', 'invoices', 'id'), ('product_id', 'products', 'id'),
                        ('tax_rate_id', 'tax_rates', 'id')],
    'bills': [('vendor_id', 'entities', 'id')],
    'bill_lines': [('bill_id', 'bills', 'id'), ('product_id', 'products', 'id'),
                    ('tax_rate_id', 'tax_rates', 'id')],
    'invoice_payments': [('payment_method_id', 'payment_methods', 'id'), ('invoice_id', 'invoices', 'id')],
    'bill_payments': [('payment_method_id', 'payment_methods', 'id'), ('bill_id', 'bills', 'id')],
    'bank_transactions': [('bank_account_id', 'bank_accounts', 'id'), ('journal_id', 'journals', 'id'),
                            ('invoice_payment_id', 'invoice_payments', 'id'), ('bill_payment_id', 'bill_payments', 'id')]
}

acctg_set2 = {
    "excel_path" : "acctg_db2/acctg_export2.xlsx", 
    "sql_output_path" : "acctg_db2/accounting.sql", 
    "db_path" : "acctg_db2/accounting.db"
}

fk2 = {
    'accounts': [('account_type_id', 'account_types', 'id'), ('parent_account_id', 'accounts', 'id')],
    'entities': [('type_id', 'entity_types', 'id')],
    'bank_accounts': [('account_id', 'accounts', 'id'), ('currency_id', 'currencies', 'id')],
    'journal_lines': [('journal_id', 'journals', 'id'), ('account_id', 'accounts', 'id')],
    'products': [('category_id', 'product_categories', 'id'), ('tax_rate_id', 'tax_rates', 'id'),
                    ('inventory_account_id', 'accounts', 'id'), ('revenue_account_id', 'accounts', 'id'),
                    ('expense_account_id', 'accounts', 'id')],
    'invoices': [('customer_id', 'entities', 'id')],
    'invoice_lines': [('invoice_id', 'invoices', 'id'), ('product_id', 'products', 'id'),
                        ('tax_rate_id', 'tax_rates', 'id')],
    'bills': [('vendor_id', 'entities', 'id')],
    'bill_lines': [('bill_id', 'bills', 'id'), ('product_id', 'products', 'id'),
                    ('tax_rate_id', 'tax_rates', 'id')],
    'cash_transactions': [('payment_method_id', 'payment_methods', 'id'), ('invoice_id', 'invoices', 'id'), ('bill_id', 'bills', 'id'), ('cash_id', 'accounts', 'id'), ('account_id', 'accounts', 'id')],
    'bank_transactions': [('bank_account_id', 'bank_accounts', 'id'), ('cash_transaction_id', 'cash_transactions', 'id')]
}

acctg_set3 = {
    "excel_path" : "acctg_db3/acctg_export3.xlsx", 
    "sql_output_path" : "acctg_db3/accounting.sql", 
    "db_path" : "acctg_db3/accounting.db"
}

fk3 = {
    'accounts': [('account_type_id', 'account_types', 'id'), ('parent_account_id', 'accounts', 'id')],
    'entities': [('type_id', 'entity_types', 'id')],
    'bank_accounts': [('account_id', 'accounts', 'id'), ('currency_id', 'currencies', 'id')],
    'journal_lines': [('journal_id', 'journals', 'id'), ('account_id', 'accounts', 'id')],
    'products': [('tax_rate_id', 'tax_rates', 'id'),
                    ('inventory_account_id', 'accounts', 'id'), ('revenue_account_id', 'accounts', 'id'),
                    ('expense_account_id', 'accounts', 'id')],
    'invoices': [('customer_id', 'entities', 'id')],
    'invoice_lines': [('invoice_id', 'invoices', 'id'), ('product_id', 'products', 'id'),
                        ('tax_rate_id', 'tax_rates', 'id'), ('account_id', 'accounts', 'id')],
    'bills': [('vendor_id', 'entities', 'id')],
    'bill_lines': [('bill_id', 'bills', 'id'), ('product_id', 'products', 'id'),
                    ('tax_rate_id', 'tax_rates', 'id'), ('account_id', 'accounts', 'id')],
    'cash_transactions': [('payment_method_id', 'payment_methods', 'id'), ('invoice_id', 'invoices', 'id'), ('bill_id', 'bills', 'id'), ('cash_id', 'accounts', 'id'), ('account_id', 'accounts', 'id'), ('tax_rate_id', 'tax_rates', 'id')],
    'bank_transactions': [('bank_account_id', 'bank_accounts', 'id'), ('cash_transaction_id', 'cash_transactions', 'id')]
}


acctg_set4 = {
    "excel_path" : "acctg_db4/acctg_export4.xlsx", 
    "sql_output_path" : "../assets/database/accounting.sql", 
    "db_path" : "../assets/database/accounting.db"
}

fk4 = {
    'accounts': [('account_type_id', 'account_types', 'id'), ('parent_account_id', 'accounts', 'id')],
    'contacts': [('type_id', 'contact_types', 'id')],
    'bank_accounts': [('account_id', 'accounts', 'id'), ('currency_id', 'currencies', 'id')],
    'journal_lines': [('journal_id', 'journals', 'id'), ('account_id', 'accounts', 'id')],
    'products': [('tax_rate_id', 'tax_rates', 'id'),
                    ('inventory_account_id', 'accounts', 'id'), ('revenue_account_id', 'accounts', 'id'),
                    ('expense_account_id', 'accounts', 'id')],
    'invoices': [('customer_id', 'contacts', 'id')],
    'invoice_lines': [('invoice_id', 'invoices', 'id'), ('product_id', 'products', 'id'),
                        ('tax_rate_id', 'tax_rates', 'id'), ('account_id', 'accounts', 'id')],
    'invoice_payments': [('invoice_id', 'invoices', 'id'), ('payment_method_id', 'payment_methods', 'id'),
                        ('account_id', 'accounts', 'id')],
    'bills': [('vendor_id', 'contacts', 'id')],
    'bill_lines': [('bill_id', 'bills', 'id'), ('product_id', 'products', 'id'),
                    ('tax_rate_id', 'tax_rates', 'id'), ('account_id', 'accounts', 'id')],
    'bill_payments': [('bill_id', 'bills', 'id'), ('payment_method_id', 'payment_methods', 'id'),
                        ('account_id', 'accounts', 'id')],
    'cash_transactions': [('contact_id', 'contacts', 'id'), ('tax_rate_id', 'tax_rates', 'id'),
                          ('payment_method_id', 'payment_methods', 'id'), ('account_id', 'accounts', 'id')],
    'cash_transaction_lines': [('cash_transaction_id', 'cash_transactions', 'id'), ('product_id', 'products', 'id'),
                          ('tax_rate_id', 'tax_rates', 'id'), ('account_id', 'accounts', 'id')],
    'bank_transactions': [('bank_account_id', 'bank_accounts', 'id'), ('cash_transaction_id', 'cash_transactions', 'id'),
                          ('invoice_payment_id', 'invoice_payments', 'id'), ('bill_payment_id', 'bill_payments', 'id')]
}
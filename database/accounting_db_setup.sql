-- Accounting Database Schema

-- Chart of Accounts
CREATE TABLE account_types (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    account_type_id INTEGER NOT NULL,
    parent_account_id INTEGER,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_type_id) REFERENCES account_types(id),
    FOREIGN KEY (parent_account_id) REFERENCES accounts(id)
);

-- Contacts (Customers, Vendors, Employees)
CREATE TABLE contact_types (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE contacts (
    id INTEGER PRIMARY KEY,
    type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    company_name TEXT,
    tax_number TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    country TEXT,
    phone TEXT,
    email TEXT,
    website TEXT,
    notes TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES contact_types(id)
);

-- Fiscal Periods -- not used?
CREATE TABLE fiscal_years (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_closed BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Currencies
CREATE TABLE currencies (
    id INTEGER PRIMARY KEY,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    symbol TEXT NOT NULL,
    is_default BOOLEAN DEFAULT 0
);

-- Tax Rates
CREATE TABLE tax_rates (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rate DECIMAL(10,2) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT 1
);

-- Payment Methods
CREATE TABLE payment_methods (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    is_active BOOLEAN DEFAULT 1
);

-- Bank Accounts
CREATE TABLE bank_accounts (
    id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    bank_name TEXT NOT NULL,
    account_number TEXT NOT NULL,
    description TEXT,
    currency_id INTEGER NOT NULL,
    opening_balance DECIMAL(15,2) DEFAULT 0,
    current_balance DECIMAL(15,2) DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(id),
    FOREIGN KEY (currency_id) REFERENCES currencies(id)
);

-- Journal Entries
CREATE TABLE journal_entries (
    id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    entry_number TEXT NOT NULL UNIQUE,
    description TEXT,
    notes TEXT,
    -- fiscal_year_id INTEGER,
    is_posted BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    -- FOREIGN KEY (fiscal_year_id) REFERENCES fiscal_years(id)
);

CREATE TABLE journal_entry_lines (
    id INTEGER PRIMARY KEY,
    journal_entry_id INTEGER NOT NULL,
    account_id INTEGER NOT NULL,
    description TEXT,
    debit DECIMAL(15,2) DEFAULT 0,
    credit DECIMAL(15,2) DEFAULT 0,
    FOREIGN KEY (journal_entry_id) REFERENCES journal_entries(id),
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);

-- Products/Items
CREATE TABLE product_categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    sku TEXT NOT NULL UNIQUE,
    category_id INTEGER,
    sale_price DECIMAL(15,2) DEFAULT 0,
    purchase_price DECIMAL(15,2) DEFAULT 0,
    tax_rate_id INTEGER,
    is_active BOOLEAN DEFAULT 1,
    -- inventory_tracking
    inventory_tracking INTEGER,
    current_stock INTEGER,
    reorder_level INTEGER,
    inventory_account_id INTEGER,
    revenue_account_id INTEGER,
    expense_account_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_categories(id),
    FOREIGN KEY (tax_rate_id) REFERENCES tax_rates(id),
    FOREIGN KEY (inventory_account_id) REFERENCES accounts(id),
    FOREIGN KEY (revenue_account_id) REFERENCES accounts(id),
    FOREIGN KEY (expense_account_id) REFERENCES accounts(id)
);

-- Invoices (Sales)
CREATE TABLE invoices (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    invoice_number TEXT NOT NULL UNIQUE,
    date DATE NOT NULL,
    due_date DATE NOT NULL,
    total_amount DECIMAL(15,2) DEFAULT 0,
    tax_amount DECIMAL(15,2) DEFAULT 0,
    notes TEXT,
    status TEXT DEFAULT 'draft', -- draft, sent, paid, partially_paid, overdue, cancelled
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES contacts(id)
);

CREATE TABLE invoice_lines (
    id INTEGER PRIMARY KEY,
    invoice_id INTEGER NOT NULL,
    product_id INTEGER,
    description TEXT NOT NULL,
    quantity DECIMAL(15,2) NOT NULL,
    unit_price DECIMAL(15,2) NOT NULL,
    tax_rate_id INTEGER,
    tax_amount DECIMAL(15,2) DEFAULT 0,
    line_total DECIMAL(15,2) DEFAULT 0,
    FOREIGN KEY (invoice_id) REFERENCES invoices(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (tax_rate_id) REFERENCES tax_rates(id)
);

-- Bills (Purchases)
CREATE TABLE bills (
    id INTEGER PRIMARY KEY,
    vendor_id INTEGER NOT NULL,
    bill_number TEXT NOT NULL UNIQUE,
    date DATE NOT NULL,
    due_date DATE NOT NULL,
    total_amount DECIMAL(15,2) DEFAULT 0,
    tax_amount DECIMAL(15,2) DEFAULT 0,
    notes TEXT,
    status TEXT DEFAULT 'draft', -- draft, received, paid, partially_paid, overdue, cancelled
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vendor_id) REFERENCES contacts(id)
);

CREATE TABLE bill_lines (
    id INTEGER PRIMARY KEY,
    bill_id INTEGER NOT NULL,
    product_id INTEGER,
    description TEXT NOT NULL,
    quantity DECIMAL(15,2) NOT NULL,
    unit_price DECIMAL(15,2) NOT NULL,
    tax_rate_id INTEGER,
    tax_amount DECIMAL(15,2) DEFAULT 0,
    line_total DECIMAL(15,2) DEFAULT 0,
    FOREIGN KEY (bill_id) REFERENCES bills(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (tax_rate_id) REFERENCES tax_rates(id)
);

-- Payments
-- CREATE TABLE payments (
--     id INTEGER PRIMARY KEY,
--     payment_number TEXT NOT NULL UNIQUE,
--     date DATE NOT NULL,
--     amount DECIMAL(15,2) NOT NULL,
--     payment_method_id INTEGER NOT NULL,
--     reference TEXT,
--     notes TEXT,
--     bank_account_id INTEGER,
--     journal_entry_id INTEGER,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id),
--     FOREIGN KEY (bank_account_id) REFERENCES bank_accounts(id),
--     FOREIGN KEY (journal_entry_id) REFERENCES journal_entries(id)
-- );

CREATE TABLE invoice_payments (
    id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    invoice_id INTEGER NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    reference TEXT,
    notes TEXT,
    payment_method_id INTEGER NOT NULL,
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id),
    FOREIGN KEY (invoice_id) REFERENCES invoices(id)
);

CREATE TABLE bill_payments (
    id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    bill_id INTEGER NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    reference TEXT,
    notes TEXT,
    payment_method_id INTEGER NOT NULL,
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id),
    FOREIGN KEY (bill_id) REFERENCES bills(id)
);

-- Bank Reconciliation
-- CREATE TABLE bank_statements (
--     id INTEGER PRIMARY KEY,
--     bank_account_id INTEGER NOT NULL,
--     statement_date DATE NOT NULL,
--     start_date DATE NOT NULL,
--     end_date DATE NOT NULL,
--     starting_balance DECIMAL(15,2) NOT NULL,
--     ending_balance DECIMAL(15,2) NOT NULL,
--     is_reconciled BOOLEAN DEFAULT 0,
--     reconciled_at TIMESTAMP,
--     notes TEXT,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (bank_account_id) REFERENCES bank_accounts(id)
-- );

CREATE TABLE bank_transactions (
    id INTEGER PRIMARY KEY,
    bank_account_id INTEGER NOT NULL,
    date DATE NOT NULL,
    description TEXT NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    type TEXT NOT NULL, -- deposit, withdrawal
    reference TEXT,
    is_reconciled BOOLEAN DEFAULT 0,
    journal_entry_id INTEGER,
    invoice_payment_id INTEGER,
    bill_payment_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bank_account_id) REFERENCES bank_accounts(id)
    FOREIGN KEY (journal_entry_id) REFERENCES journal_entries(id)
    FOREIGN KEY (invoice_payment_id) REFERENCES invoice_payments(id)
    FOREIGN KEY (bill_payment_id) REFERENCES bill_payments(id)
);
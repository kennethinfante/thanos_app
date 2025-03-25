CREATE TABLE IF NOT EXISTS account_types (
id INTEGER PRIMARY KEY,
name TEXT,
description TEXT
);

CREATE TABLE IF NOT EXISTS accounts (
id INTEGER PRIMARY KEY,
code TEXT NOT NULL UNIQUE,
name TEXT,
description TEXT,
account_type_id INTEGER,
parent_account_id INTEGER,
is_active BOOLEAN DEFAULT 1,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (account_type_id) REFERENCES account_types(id),
FOREIGN KEY (parent_account_id) REFERENCES accounts(id)
);

CREATE TABLE IF NOT EXISTS contact_types (
id INTEGER PRIMARY KEY,
name TEXT
);

CREATE TABLE IF NOT EXISTS contacts (
id INTEGER PRIMARY KEY,
type_id INTEGER,
name TEXT,
company_name TEXT,
contact_number TEXT NOT NULL UNIQUE,
tax_number TEXT NOT NULL UNIQUE,
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

CREATE TABLE IF NOT EXISTS fiscal_years (
id INTEGER PRIMARY KEY,
name TEXT,
start_date TEXT,
end_date TEXT,
is_closed BOOLEAN DEFAULT 0,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
first_name TEXT,
middle_name TEXT,
last_name TEXT,
phone_number TEXT NOT NULL UNIQUE,
address TEXT,
gender TEXT,
email TEXT,
password TEXT
);

CREATE TABLE IF NOT EXISTS currencies (
id INTEGER PRIMARY KEY,
code TEXT NOT NULL UNIQUE,
name TEXT,
symbol TEXT,
is_default BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS tax_rates (
id INTEGER PRIMARY KEY,
name TEXT,
rate TEXT,
description TEXT,
is_active BOOLEAN DEFAULT 1
);

CREATE TABLE IF NOT EXISTS payment_methods (
id INTEGER PRIMARY KEY,
name TEXT,
is_active BOOLEAN DEFAULT 1
);

CREATE TABLE IF NOT EXISTS bank_accounts (
id INTEGER PRIMARY KEY,
account_id INTEGER,
bank_name TEXT,
account_number TEXT NOT NULL UNIQUE,
description TEXT,
currency_id INTEGER,
opening_balance DECIMAL(15,2) DEFAULT 0,
current_balance DECIMAL(15,2) DEFAULT 0,
is_active BOOLEAN DEFAULT 1,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (account_id) REFERENCES accounts(id),
FOREIGN KEY (currency_id) REFERENCES currencies(id)
);

CREATE TABLE IF NOT EXISTS journal_entries (
id INTEGER PRIMARY KEY,
date TEXT,
entry_number TEXT NOT NULL UNIQUE,
description TEXT,
notes TEXT,
is_posted BOOLEAN DEFAULT 0,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS journal_entry_lines (
id INTEGER PRIMARY KEY,
journal_entry_id INTEGER,
account_id INTEGER,
description TEXT,
debit DECIMAL(15,2) DEFAULT 0,
credit DECIMAL(15,2) DEFAULT 0,
FOREIGN KEY (journal_entry_id) REFERENCES journal_entries(id),
FOREIGN KEY (account_id) REFERENCES accounts(id)
);

CREATE TABLE IF NOT EXISTS product_categories (
id INTEGER PRIMARY KEY,
name TEXT,
description TEXT
);

CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY,
name TEXT,
description TEXT,
sku TEXT NOT NULL UNIQUE,
category_id INTEGER,
sale_price DECIMAL(15,2) DEFAULT 0,
purchase_price DECIMAL(15,2) DEFAULT 0,
tax_rate_id INTEGER,
is_active BOOLEAN DEFAULT 1,
inventory_tracking TEXT,
current_stock TEXT,
reorder_level TEXT,
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

CREATE TABLE IF NOT EXISTS invoices (
id INTEGER PRIMARY KEY,
customer_id INTEGER,
invoice_number TEXT NOT NULL UNIQUE,
date TEXT,
due_date TEXT,
total_amount DECIMAL(15,2) DEFAULT 0,
tax_amount DECIMAL(15,2) DEFAULT 0,
notes TEXT,
status TEXT DEFAULT 'draft', -- draft, sent, paid, partially_paid, overdue, cancelled,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (customer_id) REFERENCES contacts(id)
);

CREATE TABLE IF NOT EXISTS invoice_lines (
id INTEGER PRIMARY KEY,
invoice_id INTEGER,
product_id INTEGER,
description TEXT,
quantity TEXT,
unit_price DECIMAL(15,2) DEFAULT 0,
tax_rate_id INTEGER,
tax_amount DECIMAL(15,2) DEFAULT 0,
line_amount DECIMAL(15,2) DEFAULT 0,
FOREIGN KEY (invoice_id) REFERENCES invoices(id),
FOREIGN KEY (product_id) REFERENCES products(id),
FOREIGN KEY (tax_rate_id) REFERENCES tax_rates(id)
);

CREATE TABLE IF NOT EXISTS bills (
id INTEGER PRIMARY KEY,
vendor_id INTEGER,
bill_number TEXT NOT NULL UNIQUE,
date TEXT,
due_date TEXT,
total_amount DECIMAL(15,2) DEFAULT 0,
tax_amount DECIMAL(15,2) DEFAULT 0,
notes TEXT,
status TEXT DEFAULT 'draft', -- draft, received, paid, partially_paid, overdue, cancelled,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (vendor_id) REFERENCES contacts(id)
);

CREATE TABLE IF NOT EXISTS bill_lines (
id INTEGER PRIMARY KEY,
bill_id INTEGER,
product_id INTEGER,
description TEXT,
quantity TEXT,
unit_price DECIMAL(15,2) DEFAULT 0,
tax_rate_id INTEGER,
tax_amount DECIMAL(15,2) DEFAULT 0,
line_amount DECIMAL(15,2) DEFAULT 0,
FOREIGN KEY (bill_id) REFERENCES bills(id),
FOREIGN KEY (product_id) REFERENCES products(id),
FOREIGN KEY (tax_rate_id) REFERENCES tax_rates(id)
);

CREATE TABLE IF NOT EXISTS invoice_payments (
id INTEGER PRIMARY KEY,
date TEXT,
invoice_id INTEGER,
amount DECIMAL(15,2) DEFAULT 0,
reference TEXT,
notes TEXT,
payment_method_id INTEGER,
FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id),
FOREIGN KEY (invoice_id) REFERENCES invoices(id)
);

CREATE TABLE IF NOT EXISTS bill_payments (
id INTEGER PRIMARY KEY,
date TEXT,
bill_id INTEGER,
amount DECIMAL(15,2) DEFAULT 0,
reference TEXT,
notes TEXT,
payment_method_id INTEGER,
FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id),
FOREIGN KEY (bill_id) REFERENCES bills(id)
);

CREATE TABLE IF NOT EXISTS bank_transactions (
id INTEGER PRIMARY KEY,
bank_account_id INTEGER,
date TEXT,
description TEXT,
amount DECIMAL(15,2) DEFAULT 0,
type TEXT,
reference TEXT,
is_reconciled BOOLEAN DEFAULT 0,
journal_entry_id INTEGER,
invoice_payment_id INTEGER,
bill_payment_id INTEGER,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (bank_account_id) REFERENCES bank_accounts(id),
FOREIGN KEY (journal_entry_id) REFERENCES journal_entries(id),
FOREIGN KEY (invoice_payment_id) REFERENCES invoice_payments(id),
FOREIGN KEY (bill_payment_id) REFERENCES bill_payments(id)
);

INSERT INTO account_types (id, name, description) VALUES (
(1, "Assets", "Resources owned by the business"),
(2, "Liabilities", "Debts owed by the business"),
(3, "Equity", "Owner's interest in the business"),
(4, "Revenue", "Income from business activities"),
(5, "Expenses", "Costs incurred in business operations"),
);

INSERT INTO accounts (id, code, name, description, account_type_id, parent_account_id, is_active, created_at) VALUES (
(1, 1000, "Assets", "All assets", 1, NULL, 1, "2025-03-24 06:31:20"),
(2, 1100, "Current Assets", "Short-term assets", 1, "1.0", 1, "2025-03-24 06:31:20"),
(3, 1110, "Cash and Cash Equivalents", "Cash and liquid assets", 1, "2.0", 1, "2025-03-24 06:31:20"),
(4, 1111, "Cash on Hand", "Physical cash", 1, "3.0", 1, "2025-03-24 06:31:20"),
(5, 1112, "Checking Account", "Main business checking", 1, "3.0", 1, "2025-03-24 06:31:20"),
(6, 1113, "Savings Account", "Business savings", 1, "3.0", 1, "2025-03-24 06:31:20"),
(7, 1120, "Accounts Receivable", "Money owed by customers", 1, "2.0", 1, "2025-03-24 06:31:20"),
(8, 1130, "Inventory", "Goods for sale", 1, "2.0", 1, "2025-03-24 06:31:20"),
(9, 1140, "Prepaid Expenses", "Expenses paid in advance", 1, "2.0", 1, "2025-03-24 06:31:20"),
(10, 1200, "Fixed Assets", "Long-term assets", 1, "1.0", 1, "2025-03-24 06:31:20"),
(11, 1210, "Equipment", "Business equipment", 1, "10.0", 1, "2025-03-24 06:31:20"),
(12, 1220, "Furniture and Fixtures", "Office furniture", 1, "10.0", 1, "2025-03-24 06:31:20"),
(13, 1230, "Vehicles", "Company vehicles", 1, "10.0", 1, "2025-03-24 06:31:20"),
(14, 1240, "Buildings", "Company buildings", 1, "10.0", 1, "2025-03-24 06:31:20"),
(15, 1250, "Land", "Company land", 1, "10.0", 1, "2025-03-24 06:31:20"),
(16, 1260, "Accumulated Depreciation", "Accumulated depreciation", 1, "10.0", 1, "2025-03-24 06:31:20"),
(17, 2000, "Liabilities", "All liabilities", 2, NULL, 1, "2025-03-24 06:31:20"),
(18, 2100, "Current Liabilities", "Short-term liabilities", 2, "17.0", 1, "2025-03-24 06:31:20"),
(19, 2110, "Accounts Payable", "Money owed to vendors", 2, "18.0", 1, "2025-03-24 06:31:20"),
(20, 2120, "Accrued Expenses", "Expenses incurred but not paid", 2, "18.0", 1, "2025-03-24 06:31:20"),
(21, 2130, "Taxes Payable", "Taxes owed", 2, "18.0", 1, "2025-03-24 06:31:20"),
(22, 2140, "Payroll Liabilities", "Payroll-related liabilities", 2, "18.0", 1, "2025-03-24 06:31:20"),
(23, 2150, "Short-term Loans", "Loans due within one year", 2, "18.0", 1, "2025-03-24 06:31:20"),
(24, 2200, "Long-term Liabilities", "Long-term liabilities", 2, "17.0", 1, "2025-03-24 06:31:20"),
(25, 2210, "Long-term Loans", "Loans due after one year", 2, "24.0", 1, "2025-03-24 06:31:20"),
(26, 2220, "Mortgage Payable", "Mortgage on property", 2, "24.0", 1, "2025-03-24 06:31:20"),
(27, 3000, "Equity", "All equity", 3, NULL, 1, "2025-03-24 06:31:20"),
(28, 3100, "Owner's Capital", "Owner's investment", 3, "27.0", 1, "2025-03-24 06:31:20"),
(29, 3200, "Retained Earnings", "Accumulated earnings", 3, "27.0", 1, "2025-03-24 06:31:20"),
(30, 3300, "Dividends Paid", "Dividends paid to owners", 3, "27.0", 1, "2025-03-24 06:31:20"),
(31, 4000, "Revenue", "All revenue", 4, NULL, 1, "2025-03-24 06:31:20"),
(32, 4100, "Sales Revenue", "Revenue from sales", 4, "31.0", 1, "2025-03-24 06:31:20"),
(33, 4200, "Service Revenue", "Revenue from services", 4, "31.0", 1, "2025-03-24 06:31:20"),
(34, 4300, "Interest Income", "Income from interest", 4, "31.0", 1, "2025-03-24 06:31:20"),
(35, 4400, "Other Income", "Miscellaneous income", 4, "31.0", 1, "2025-03-24 06:31:20"),
(36, 5000, "Expenses", "All expenses", 5, NULL, 1, "2025-03-24 06:31:20"),
(37, 5100, "Cost of Goods Sold", "Direct costs of goods sold", 5, "36.0", 1, "2025-03-24 06:31:20"),
(38, 5200, "Salaries and Wages", "Employee compensation", 5, "36.0", 1, "2025-03-24 06:31:20"),
(39, 5300, "Rent Expense", "Office/facility rent", 5, "36.0", 1, "2025-03-24 06:31:20"),
(40, 5400, "Utilities Expense", "Electricity, water, etc.", 5, "36.0", 1, "2025-03-24 06:31:20"),
(41, 5500, "Office Supplies", "Office consumables", 5, "36.0", 1, "2025-03-24 06:31:20"),
(42, 5600, "Advertising and Marketing", "Promotional expenses", 5, "36.0", 1, "2025-03-24 06:31:20"),
(43, 5700, "Insurance Expense", "Business insurance", 5, "36.0", 1, "2025-03-24 06:31:20"),
(44, 5800, "Depreciation Expense", "Asset depreciation", 5, "36.0", 1, "2025-03-24 06:31:20"),
(45, 5900, "Interest Expense", "Interest on loans", 5, "36.0", 1, "2025-03-24 06:31:20"),
(46, 6000, "Miscellaneous Expense", "Other expenses", 5, "36.0", 1, "2025-03-24 06:31:20"),
);

INSERT INTO contact_types (id, name) VALUES (
(1, "Customer"),
(2, "Vendor"),
(3, "Employee"),
);

INSERT INTO contacts (id, type_id, name, company_name, contact_number, tax_number, address, city, state, postal_code, country, phone, email, website, notes, is_active, created_at) VALUES (
(1, 1, "John Smith", "Smith Enterprises", "C-123456", "123-45-6789", "123 Main St", "New York", "NY", 10001, "USA", "212-555-1234", "john@smith.com", "www.smithenterprises.com", "Regular customer", 1, "2025-03-24 06:31:20"),
(2, 1, "Sarah Johnson", "Johnson LLC", "C-234567", "987-65-4321", "456 Oak Ave", "Los Angeles", "CA", 90001, "USA", "310-555-5678", "sarah@johnson.com", "www.johnsonllc.com", "Premium customer", 1, "2025-03-24 06:31:20"),
(3, 1, "Michael Brown", "Brown Industries", "C-345678", "456-78-9012", "789 Pine Rd", "Chicago", "IL", 60007, "USA", "312-555-9012", "michael@brown.com", "www.brownindustries.com", "New customer", 1, "2025-03-24 06:31:20"),
(4, 1, "Emily Davis", "Davis Co.", "C-456789", "789-01-2345", "101 Elm St", "Houston", "TX", 77001, "USA", "713-555-3456", "emily@davis.com", "www.davisco.com", "Occasional customer", 1, "2025-03-24 06:31:20"),
(5, 1, "Robert Wilson", "Wilson Group", "C-567890", "234-56-7890", "202 Maple Dr", "Miami", "FL", 33101, "USA", "305-555-7890", "robert@wilson.com", "www.wilsongroup.com", "Loyal customer", 1, "2025-03-24 06:31:20"),
(6, 2, "Office Supplies Inc.", "Office Supplies Inc.", "V-123456", "321-45-6789", "100 Supply St", "Boston", "MA", 2101, "USA", "617-555-1111", "info@officesupplies.com", "www.officesupplies.com", "Office supplies vendor", 1, "2025-03-24 06:31:20"),
(7, 2, "Tech Solutions", "Tech Solutions LLC", "V-234567", "789-65-4321", "200 Tech Blvd", "San Francisco", "CA", 94101, "USA", "415-555-2222", "info@techsolutions.com", "www.techsolutions.com", "IT equipment vendor", 1, "2025-03-24 06:31:20"),
(8, 2, "Furniture World", "Furniture World Corp", "V-345678", "654-78-9012", "300 Chair Ave", "Seattle", "WA", 98101, "USA", "206-555-3333", "info@furnitureworld.com", "www.furnitureworld.com", "Office furniture vendor", 1, "2025-03-24 06:31:20"),
(9, 2, "Marketing Experts", "Marketing Experts Co.", "V-456789", "987-01-2345", "400 Ad St", "Denver", "CO", 80201, "USA", "303-555-4444", "info@marketingexperts.com", "www.marketingexperts.com", "Marketing services vendor", 1, "2025-03-24 06:31:20"),
(10, 2, "Shipping Partners", "Shipping Partners Inc.", "V-567890", "432-56-7890", "500 Delivery Rd", "Atlanta", "GA", 30301, "USA", "404-555-5555", "info@shippingpartners.com", "www.shippingpartners.com", "Shipping services vendor", 1, "2025-03-24 06:31:20"),
(11, 3, "David Miller", "ACME Corp", "E-123456", "231-45-6789", "111 Worker St", "Dallas", "TX", 75201, "USA", "214-555-6666", "david@acme.com", "www.acme.com", "Sales Manager", 1, "2025-03-24 06:31:20"),
(12, 3, "Jennifer Lee", "ACME Corp", "E-234567", "879-65-4321", "222 Staff Ave", "Phoenix", "AZ", 85001, "USA", "602-555-7777", "jennifer@acme.com", "www.acme.com", "Accountant", 1, "2025-03-24 06:31:20"),
(13, 3, "Thomas Clark", "ACME Corp", "E-345678", "645-78-9012", "333 Employee Rd", "Philadelphia", "PA", 19101, "USA", "215-555-8888", "thomas@acme.com", "www.acme.com", "Operations Manager", 1, "2025-03-24 06:31:20"),
(14, 3, "Amanda White", "ACME Corp", "E-456789", "978-01-2345", "444 Team St", "San Diego", "CA", 92101, "USA", "619-555-9999", "amanda@acme.com", "www.acme.com", "Marketing Specialist", 1, "2025-03-24 06:31:20"),
(15, 3, "James Taylor", "ACME Corp", "E-567890", "423-56-7890", "555 Colleague Dr", "Portland", "OR", 97201, "USA", "503-555-0000", "james@acme.com", "www.acme.com", "IT Specialist", 1, "2025-03-24 06:31:20"),
);

INSERT INTO fiscal_years (id, name, start_date, end_date, is_closed, created_at) VALUES (
(1, "FY 2022", "2022-01-01", "2022-12-31", 0, "2025-03-24 06:31:20"),
);

INSERT INTO users (id, first_name, middle_name, last_name, phone_number, address, gender, email, password) VALUES (
(1, "Kenneth", "Dotor", "Infante", "(112) 909-5334", "6092 Auctor, Street", "m", "kenneth@google.com", "$2b$12$H77I6FSJJ3RwmjJJ2Eql2eSCbSqwJiQxsQsfQWEWeP2FGwc7LtYJG"),
(2, "David Woodard", "Harlan", "Acton", 209268717220, "7679 Luctus Rd.", "m", "volutpat.nulla@hotmail.ca", "$2b$12$TySE.YCrRcDcFdll9SqJUeGgIM3xzHHkTJbs/3/V0QDCTygU4zn1G"),
(3, "Marvin Zamora", "Joshua", "Oren", 207555183118, "Ap #211-8021 Suspendisse Rd.", "m", "eu.enim.etiam@outlook.ca", "$2b$12$RussJqzD1obCxkaKKCkO4eTHtk7iOVRsK56CUa5Oa5P4ImTPwKM1m"),
(4, "Dorothy Wyatt", "Camden", "Brent", 208714677697, "Cherokee Horne,Hayes,Garrett,+201564537686,Ap #206-3399 Dignissim Street,malesuada.fames@hotmail.org", "f", "nunc@google.couk", "$2b$12$9eCK8.Sa.qIHCmihdX1J2eD5UJv9TqP4SyQ4HCep9odrMZgDyD3Ne"),
(5, "Cherokee Horne", "Hayes", "Garrett", 201564537686, "Ap #206-3399 Dignissim Street", "f", "malesuada.fames@hotmail.org", "$2b$12$FmVp9bq75rco7ghr8DSmD.NcUT5kQwW82gaRjprun8UPn9Z/xlcC2"),
);

INSERT INTO currencies (id, code, name, symbol, is_default) VALUES (
(1, "USD", "US Dollar", "$", 1),
(2, "EUR", "Euro", "€", 0),
(3, "GBP", "British Pound", "£", 0),
(4, "CAD", "Canadian Dollar", "C$", 0),
(5, "JPY", "Japanese Yen", "¥", 0),
);

INSERT INTO tax_rates (id, name, rate, description, is_active) VALUES (
(1, "No Tax", "0.0", "No tax applied", 1),
(2, "Sales Tax", "7.5", "Standard sales tax", 1),
(3, "Reduced Tax", "3.5", "Reduced rate for certain goods", 1),
(4, "VAT Standard", "20.0", "Standard VAT rate", 1),
(5, "VAT Reduced", "10.0", "Reduced VAT rate", 1),
);

INSERT INTO payment_methods (id, name, is_active) VALUES (
(1, "Cash", 1),
(2, "Credit Card", 1),
(3, "Bank Transfer", 1),
(4, "Check", 1),
(5, "PayPal", 1),
(6, "Other", 1),
);

INSERT INTO bank_accounts (id, account_id, bank_name, account_number, description, currency_id, opening_balance, current_balance, is_active, created_at) VALUES (
(1, 5, "First National Bank", 1234567890, "Main Checking Account", 1, 10000, 10000, 1, "2025-03-24 06:31:20"),
(2, 6, "First National Bank", 0987654321, "Savings Account", 1, 25000, 25000, 1, "2025-03-24 06:31:20"),
(3, 5, "International Bank", "EUR1234567", "Euro Account", 2, 5000, 5000, 1, "2025-03-24 06:31:20"),
);

INSERT INTO journal_entries (id, date, entry_number, description, notes, is_posted, created_at) VALUES (
(1, "2022-01-05", "JE-2022-001", "Initial capital investment", "Owner investment to start business operations", 1, "2025-03-24 06:31:25"),
(2, "2022-01-10", "JE-2022-002", "Office rent payment", "Monthly office rent", 1, "2025-03-24 06:31:25"),
(3, "2022-01-15", "JE-2022-003", "Purchase of office supplies", "Initial office supplies", 1, "2025-03-24 06:31:25"),
(4, "2022-01-20", "JE-2022-004", "Sales revenue", "First sales of the year", 1, "2025-03-24 06:31:25"),
(5, "2022-01-25", "JE-2022-005", "Utility bills payment", "Electricity and water bills", 1, "2025-03-24 06:31:25"),
(6, "2022-01-31", "JE-2022-006", "Payroll entry", "January payroll", 1, "2025-03-24 06:31:25"),
(7, "2022-02-05", "JE-2022-007", "Purchase of equipment", "New computers for office", 1, "2025-03-24 06:31:25"),
(8, "2022-02-10", "JE-2022-008", "Office rent payment", "Monthly office rent", 1, "2025-03-24 06:31:25"),
(9, "2022-02-15", "JE-2022-009", "Sales revenue", "February sales", 1, "2025-03-24 06:31:25"),
(10, "2022-02-20", "JE-2022-010", "Marketing expenses", "Online advertising campaign", 1, "2025-03-24 06:31:25"),
(11, "2022-02-25", "JE-2022-011", "Utility bills payment", "Electricity and water bills", 1, "2025-03-24 06:31:25"),
(12, "2022-02-28", "JE-2022-012", "Payroll entry", "February payroll", 1, "2025-03-24 06:31:25"),
(13, "2022-03-05", "JE-2022-013", "Insurance payment", "Annual business insurance", 1, "2025-03-24 06:31:25"),
(14, "2022-03-10", "JE-2022-014", "Office rent payment", "Monthly office rent", 1, "2025-03-24 06:31:25"),
(15, "2022-03-15", "JE-2022-015", "Sales revenue", "March sales", 1, "2025-03-24 06:31:25"),
(16, "2022-03-20", "JE-2022-016", "Purchase of inventory", "Inventory restocking", 1, "2025-03-24 06:31:25"),
(17, "2022-03-25", "JE-2022-017", "Utility bills payment", "Electricity and water bills", 1, "2025-03-24 06:31:25"),
(18, "2022-03-31", "JE-2022-018", "Payroll entry", "March payroll", 1, "2025-03-24 06:31:25"),
(19, "2022-04-05", "JE-2022-019", "Quarterly tax payment", "Q1 tax payment", 1, "2025-03-24 06:31:25"),
(20, "2022-04-10", "JE-2022-020", "Office rent payment", "Monthly office rent", 1, "2025-03-24 06:31:25"),
(21, "2022-04-15", "JE-2022-021", "Sales revenue", "April sales", 1, "2025-03-24 06:31:25"),
(22, "2022-04-20", "JE-2022-022", "Software subscription", "Annual software licenses", 1, "2025-03-24 06:31:25"),
(23, "2022-04-25", "JE-2022-023", "Utility bills payment", "Electricity and water bills", 1, "2025-03-24 06:31:25"),
(24, "2022-04-30", "JE-2022-024", "Payroll entry", "April payroll", 1, "2025-03-24 06:31:25"),
(25, "2022-05-10", "JE-2022-025", "Office rent payment", "Monthly office rent", 1, "2025-03-24 06:31:25"),
(26, "2022-05-15", "JE-2022-026", "Sales revenue", "May sales", 1, "2025-03-24 06:31:25"),
(27, "2022-05-31", "JE-2022-027", "Payroll entry", "May payroll", 1, "2025-03-24 06:31:25"),
);

INSERT INTO journal_entry_lines (id, journal_entry_id, account_id, description, debit, credit) VALUES (
(1, 1, 5, "Cash investment", 50000, 0),
(2, 1, 28, "Owner capital", 0, 50000),
(3, 2, 39, "Monthly office rent", 2000, 0),
(4, 2, 5, "Payment from checking account", 0, 2000),
(5, 3, 41, "Office supplies purchase", 500, 0),
(6, 3, 5, "Payment from checking account", 0, 500),
(7, 4, 5, "Cash from sales", 7500, 0),
(8, 4, 32, "Revenue from product sales", 0, 7500),
(9, 5, 40, "Monthly utilities", 350, 0),
(10, 5, 5, "Payment from checking account", 0, 350),
(11, 6, 38, "Monthly payroll", 12000, 0),
(12, 6, 5, "Payment from checking account", 0, 12000),
(13, 7, 11, "New office computers", 5000, 0),
(14, 7, 5, "Payment from checking account", 0, 5000),
(15, 8, 39, "Monthly office rent", 2000, 0),
(16, 8, 5, "Payment from checking account", 0, 2000),
);

INSERT INTO product_categories (id, name, description) VALUES (
(1, "Electronics", "Electronic devices and accessories"),
(2, "Office Supplies", "General office supplies"),
(3, "Furniture", "Office furniture and fixtures"),
(4, "Software", "Computer software and licenses"),
(5, "Services", "Professional services"),
);

INSERT INTO products (id, name, description, sku, category_id, sale_price, purchase_price, tax_rate_id, is_active, inventory_tracking, current_stock, reorder_level, inventory_account_id, revenue_account_id, expense_account_id, created_at) VALUES (
(1, "Laptop Computer", "Business laptop", "ELEC-001", 1, "1200.0", "900.0", 2, 1, 1, "15.0", "5.0", "8.0", 32, 37, "2025-03-24 06:31:25"),
(2, "Desktop Computer", "Office desktop", "ELEC-002", 1, "950.0", "700.0", 2, 1, 1, "10.0", "3.0", "8.0", 32, 37, "2025-03-24 06:31:25"),
(3, "Office Chair", "Ergonomic office chair", "FURN-001", 3, "250.0", "150.0", 2, 1, 1, "20.0", "5.0", "8.0", 32, 37, "2025-03-24 06:31:25"),
(4, "Office Desk", "Standard office desk", "FURN-002", 3, "350.0", "200.0", 2, 1, 1, "10.0", "3.0", "8.0", 32, 37, "2025-03-24 06:31:25"),
(5, "Printer Paper", "Letter size paper, 500 sheets", "SUPP-001", 2, "5.99", "3.5", 2, 1, 1, "100.0", "20.0", "8.0", 32, 37, "2025-03-24 06:31:25"),
(6, "Ink Cartridges", "Black ink cartridges", "SUPP-002", 2, "24.99", "15.0", 2, 1, 1, "30.0", "10.0", "8.0", 32, 37, "2025-03-24 06:31:25"),
(7, "Accounting Software", "Annual license", "SOFT-001", 4, "299.99", "299.99", 2, 1, 0, NULL, NULL, NULL, 32, 37, "2025-03-24 06:31:25"),
(8, "IT Support", "Hourly IT support", "SERV-001", 5, "75.0", "75.0", 2, 1, 0, NULL, NULL, NULL, 33, 37, "2025-03-24 06:31:25"),
(9, "Consulting Services", "Business consulting, per hour", "SERV-002", 5, "150.0", "150.0", 2, 1, 0, NULL, NULL, NULL, 33, 37, "2025-03-24 06:31:25"),
(10, "Smartphone", "Business smartphone", "ELEC-003", 1, "699.99", "500.0", 2, 1, 1, "8.0", "3.0", "8.0", 32, 37, "2025-03-24 06:31:25"),
);

INSERT INTO invoices (id, customer_id, invoice_number, date, due_date, total_amount, tax_amount, notes, status, created_at) VALUES (
(1, 1, "INV-2022-001", "2022-01-15", "2022-02-14", 2675, 175, "Computer equipment sale", "paid", "2025-03-24 06:31:25"),
(2, 2, "INV-2022-002", "2022-01-20", "2022-02-19", 4815, 315, "Office furniture purchase", "paid", "2025-03-24 06:31:25"),
(3, 3, "INV-2022-003", "2022-02-05", "2022-03-07", 1070, 70, "Software licenses", "paid", "2025-03-24 06:31:25"),
(4, 4, "INV-2022-004", "2022-02-15", "2022-03-17", 3210, 210, "IT consulting services", "paid", "2025-03-24 06:31:25"),
(5, 5, "INV-2022-005", "2022-03-01", "2022-03-31", 5350, 350, "Office equipment and supplies", "paid", "2025-03-24 06:31:25"),
(6, 1, "INV-2022-006", "2022-03-15", "2022-04-14", 2140, 140, "Computer accessories", "paid", "2025-03-24 06:31:25"),
(7, 2, "INV-2022-007", "2022-04-01", "2022-05-01", 3745, 245, "Office renovation services", "paid", "2025-03-24 06:31:25"),
(8, 3, "INV-2022-008", "2022-04-15", "2022-05-15", 1605, 105, "Software maintenance", "paid", "2025-03-24 06:31:25"),
);

INSERT INTO invoice_lines (id, invoice_id, product_id, description, quantity, unit_price, tax_rate_id, tax_amount, line_amount) VALUES (
(1, 1, 1, "Laptop Computer", 2, "1200.0", 2, "180.0", "2580.0"),
(2, 1, 6, "Ink Cartridges", 4, "24.99", 2, "7.5", "107.46"),
(3, 2, 3, "Office Chair", 10, "250.0", 2, "187.5", "2687.5"),
(4, 2, 4, "Office Desk", 5, "350.0", 2, "131.25", "1881.25"),
(5, 3, 7, "Accounting Software", 3, "299.99", 2, "67.5", "967.47"),
(6, 3, 5, "Printer Paper", 20, "5.99", 2, "8.99", "128.79"),
(7, 4, 8, "IT Support", 40, "75.0", 2, "225.0", "3225.0"),
(8, 5, 2, "Desktop Computer", 5, "950.0", 2, "356.25", "5106.25"),
(9, 5, 6, "Ink Cartridges", 10, "24.99", 2, "18.74", "268.64"),
);

INSERT INTO bills (id, vendor_id, bill_number, date, due_date, total_amount, tax_amount, notes, status, created_at) VALUES (
(1, 6, "BILL-2022-001", "2022-01-05", "2022-02-04", 535, 35, "Office supplies purchase", "paid", "2025-03-24 06:31:25"),
(2, 7, "BILL-2022-002", "2022-01-15", "2022-02-14", 3210, 210, "IT equipment purchase", "paid", "2025-03-24 06:31:25"),
(3, 8, "BILL-2022-003", "2022-02-01", "2022-03-03", 2140, 140, "Office furniture purchase", "paid", "2025-03-24 06:31:25"),
(4, 9, "BILL-2022-004", "2022-02-15", "2022-03-17", 1070, 70, "Marketing services", "paid", "2025-03-24 06:31:25"),
(5, 10, "BILL-2022-005", "2022-03-01", "2022-03-31", 428, 28, "Office supplies restock", "paid", "2025-03-24 06:31:25"),
(6, 6, "BILL-2022-006", "2022-03-15", "2022-04-14", 1605, 105, "Computer accessories", "paid", "2025-03-24 06:31:25"),
(7, 7, "BILL-2022-007", "2022-04-01", "2022-05-01", 2675, 175, "Software licenses", "paid", "2025-03-24 06:31:25"),
(8, 8, "BILL-2022-008", "2022-04-15", "2022-05-15", 3745, 245, "Office renovation", "paid", "2025-03-24 06:31:25"),
);

INSERT INTO bill_lines (id, bill_id, product_id, description, quantity, unit_price, tax_rate_id, tax_amount, line_amount) VALUES (
(1, 1, 5, "Printer Paper", 50, "5.99", 2, "22.46", "321.96"),
(2, 1, 6, "Ink Cartridges", 8, "24.99", 2, "14.99", "214.91"),
(3, 2, 1, "Laptop Computer", 2, "1200.0", 2, "180.0", "2580.0"),
(4, 2, 10, "Smartphone", 1, "699.99", 2, "52.5", "752.49"),
(5, 3, 3, "Office Chair", 5, "250.0", 2, "93.75", "1343.75"),
(6, 3, 4, "Office Desk", 2, "350.0", 2, "52.5", "752.5"),
(7, 4, 9, "Consulting Services", 7, "150.0", 2, "78.75", "1128.75"),
(8, 5, 5, "Printer Paper", 40, "5.99", 2, "17.97", "257.57"),
(9, 5, 6, "Ink Cartridges", 7, "24.99", 2, "13.12", "188.05"),
);

INSERT INTO invoice_payments (id, date, invoice_id, amount, reference, notes, payment_method_id) VALUES (
(1, "2022-01-20", 1, 2675, "IP-2022-001", "Payment for INV-2022-001", 3),
(2, "2022-01-25", 2, 4815, "IP-2022-002", "Payment for INV-2022-002", 2),
(3, "2022-02-10", 3, 1070, "IP-2022-003", "Payment for INV-2022-003", 3),
(4, "2022-02-20", 4, 3210, "IP-2022-004", "Payment for INV-2022-004", 2),
(5, "2022-03-05", 5, 5350, "IP-2022-005", "Payment for INV-2022-005", 3),
(6, "2022-03-20", 1, 2140, "IP-2022-006", "Payment for INV-2022-006", 2),
(7, "2022-04-05", 2, 3745, "IP-2022-007", "Payment for INV-2022-007", 3),
(8, "2022-04-20", 3, 1605, "IP-2022-008", "Payment for INV-2022-008", 2),
);

INSERT INTO bill_payments (id, date, bill_id, amount, reference, notes, payment_method_id) VALUES (
(1, "2022-01-15", 1, 535, "BP-2022-001", "Payment for BILL-2022-001", 3),
(2, "2022-01-25", 2, 3210, "BP-2022-002", "Payment for BILL-2022-002", 2),
(3, "2022-02-10", 3, 2140, "BP-2022-003", "Payment for BILL-2022-003", 3),
(4, "2022-02-25", 4, 1070, "BP-2022-004", "Payment for BILL-2022-004", 2),
(5, "2022-03-10", 5, 428, "BP-2022-005", "Payment for BILL-2022-005", 3),
(6, "2022-03-25", 6, 1605, "BP-2022-006", "Payment for BILL-2022-006", 2),
(7, "2022-04-10", 7, 2675, "BP-2022-007", "Payment for BILL-2022-007", 3),
(8, "2022-04-25", 8, 3745, "BP-2022-008", "Payment for BILL-2022-008", 2),
);

INSERT INTO bank_transactions (id, bank_account_id, date, description, amount, type, reference, is_reconciled, journal_entry_id, invoice_payment_id, bill_payment_id, created_at) VALUES (
(1, 1, "2022-01-05", "Initial capital investment", 50000, "deposit", NULL, 1, "1.0", NULL, NULL, "2025-03-24 06:37:47"),
(2, 1, "2022-01-10", "Office rent payment", "-2000", "withdrawal", NULL, 1, "2.0", NULL, NULL, "2025-03-24 06:37:47"),
(3, 1, "2022-01-15", "Purchase of office supplies", "-500", "withdrawal", NULL, 1, "3.0", NULL, NULL, "2025-03-24 06:37:47"),
(4, 1, "2022-01-15", "Payment for BILL-2022-001", "-535", "withdrawal", NULL, 1, NULL, NULL, "1.0", "2025-03-24 06:37:47"),
(5, 1, "2022-01-20", "Sales revenue", 7500, "deposit", NULL, 1, "4.0", NULL, NULL, "2025-03-24 06:37:47"),
(6, 1, "2022-01-20", "Payment received for INV-2022-001", 2675, "deposit", NULL, 1, NULL, "1.0", NULL, "2025-03-24 06:37:47"),
(7, 1, "2022-01-25", "Utility bills payment", "-350", "withdrawal", NULL, 1, "5.0", NULL, NULL, "2025-03-24 06:37:47"),
(8, 1, "2022-01-25", "Payment for BILL-2022-002", "-3210", "withdrawal", NULL, 1, NULL, NULL, "2.0", "2025-03-24 06:37:47"),
(9, 1, "2022-01-25", "Payment received for INV-2022-002", 4815, "deposit", NULL, 1, NULL, "2.0", NULL, "2025-03-24 06:37:47"),
(10, 1, "2022-01-31", "Payroll entry", "-12000", "withdrawal", NULL, 1, "6.0", NULL, NULL, "2025-03-24 06:37:47"),
(11, 1, "2022-02-05", "Purchase of equipment", "-5000", "withdrawal", NULL, 1, "7.0", NULL, NULL, "2025-03-24 06:37:47"),
(12, 1, "2022-02-10", "Office rent payment", "-2000", "withdrawal", NULL, 1, "8.0", NULL, NULL, "2025-03-24 06:37:47"),
(13, 1, "2022-02-10", "Payment for BILL-2022-003", "-2140", "withdrawal", NULL, 1, NULL, NULL, "3.0", "2025-03-24 06:37:47"),
(14, 1, "2022-02-10", "Payment received for INV-2022-003", 1070, "deposit", NULL, 1, NULL, "3.0", NULL, "2025-03-24 06:37:47"),
);


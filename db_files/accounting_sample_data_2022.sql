-- Sample Data for 2022

-- Account Types
INSERT INTO account_types (id, name, description) VALUES
(1, 'Assets', 'Resources owned by the business'),
(2, 'Liabilities', 'Debts owed by the business'),
(3, 'Equity', 'Owner''s interest in the business'),
(4, 'Revenue', 'Income from business activities'),
(5, 'Expenses', 'Costs incurred in business operations');

-- Accounts
INSERT INTO accounts (code, name, description, account_type_id, parent_account_id) VALUES
-- Assets
('1000', 'Assets', 'All assets', 1, NULL),
('1100', 'Current Assets', 'Short-term assets', 1, 1),
('1110', 'Cash and Cash Equivalents', 'Cash and liquid assets', 1, 2),
('1111', 'Cash on Hand', 'Physical cash', 1, 3),
('1112', 'Checking Account', 'Main business checking', 1, 3),
('1113', 'Savings Account', 'Business savings', 1, 3),
('1120', 'Accounts Receivable', 'Money owed by customers', 1, 2),
('1130', 'Inventory', 'Goods for sale', 1, 2),
('1140', 'Prepaid Expenses', 'Expenses paid in advance', 1, 2),
('1200', 'Fixed Assets', 'Long-term assets', 1, 1),
('1210', 'Equipment', 'Business equipment', 1, 10),
('1220', 'Furniture and Fixtures', 'Office furniture', 1, 10),
('1230', 'Vehicles', 'Company vehicles', 1, 10),
('1240', 'Buildings', 'Company buildings', 1, 10),
('1250', 'Land', 'Company land', 1, 10),
('1260', 'Accumulated Depreciation', 'Accumulated depreciation', 1, 10),

-- Liabilities
('2000', 'Liabilities', 'All liabilities', 2, NULL),
('2100', 'Current Liabilities', 'Short-term liabilities', 2, 17),
('2110', 'Accounts Payable', 'Money owed to vendors', 2, 18),
('2120', 'Accrued Expenses', 'Expenses incurred but not paid', 2, 18),
('2130', 'Taxes Payable', 'Taxes owed', 2, 18),
('2140', 'Payroll Liabilities', 'Payroll-related liabilities', 2, 18),
('2150', 'Short-term Loans', 'Loans due within one year', 2, 18),
('2200', 'Long-term Liabilities', 'Long-term liabilities', 2, 17),
('2210', 'Long-term Loans', 'Loans due after one year', 2, 24),
('2220', 'Mortgage Payable', 'Mortgage on property', 2, 24),

-- Equity
('3000', 'Equity', 'All equity', 3, NULL),
('3100', 'Owner''s Capital', 'Owner''s investment', 3, 27),
('3200', 'Retained Earnings', 'Accumulated earnings', 3, 27),
('3300', 'Dividends Paid', 'Dividends paid to owners', 3, 27),

-- Revenue
('4000', 'Revenue', 'All revenue', 4, NULL),
('4100', 'Sales Revenue', 'Revenue from sales', 4, 31),
('4200', 'Service Revenue', 'Revenue from services', 4, 31),
('4300', 'Interest Income', 'Income from interest', 4, 31),
('4400', 'Other Income', 'Miscellaneous income', 4, 31),

-- Expenses
('5000', 'Expenses', 'All expenses', 5, NULL),
('5100', 'Cost of Goods Sold', 'Direct costs of goods sold', 5, 36),
('5200', 'Salaries and Wages', 'Employee compensation', 5, 36),
('5300', 'Rent Expense', 'Office/facility rent', 5, 36),
('5400', 'Utilities Expense', 'Electricity, water, etc.', 5, 36),
('5500', 'Office Supplies', 'Office consumables', 5, 36),
('5600', 'Advertising and Marketing', 'Promotional expenses', 5, 36),
('5700', 'Insurance Expense', 'Business insurance', 5, 36),
('5800', 'Depreciation Expense', 'Asset depreciation', 5, 36),
('5900', 'Interest Expense', 'Interest on loans', 5, 36),
('6000', 'Miscellaneous Expense', 'Other expenses', 5, 36);

-- Contact Types
INSERT INTO contact_types (id, name) VALUES
(1, 'Customer'),
(2, 'Vendor'),
(3, 'Employee');

-- Contacts TODO
INSERT INTO contacts (type_id, name, company_name, tax_number, address, city, state, postal_code, country, phone, email, website, notes) VALUES
-- Customers
(1, 'John Smith', 'Smith Enterprises', '123-45-6789', '123 Main St', 'New York', 'NY', '10001', 'USA', '212-555-1234', 'john@smith.com', 'www.smithenterprises.com', 'Regular customer'),
(1, 'Sarah Johnson', 'Johnson LLC', '987-65-4321', '456 Oak Ave', 'Los Angeles', 'CA', '90001', 'USA', '310-555-5678', 'sarah@johnson.com', 'www.johnsonllc.com', 'Premium customer'),
(1, 'Michael Brown', 'Brown Industries', '456-78-9012', '789 Pine Rd', 'Chicago', 'IL', '60007', 'USA', '312-555-9012', 'michael@brown.com', 'www.brownindustries.com', 'New customer'),
(1, 'Emily Davis', 'Davis Co.', '789-01-2345', '101 Elm St', 'Houston', 'TX', '77001', 'USA', '713-555-3456', 'emily@davis.com', 'www.davisco.com', 'Occasional customer'),
(1, 'Robert Wilson', 'Wilson Group', '234-56-7890', '202 Maple Dr', 'Miami', 'FL', '33101', 'USA', '305-555-7890', 'robert@wilson.com', 'www.wilsongroup.com', 'Loyal customer'),

-- Vendors
(2, 'Office Supplies Inc.', 'Office Supplies Inc.', 'V-123456', '100 Supply St', 'Boston', 'MA', '02101', 'USA', '617-555-1111', 'info@officesupplies.com', 'www.officesupplies.com', 'Office supplies vendor'),
(2, 'Tech Solutions', 'Tech Solutions LLC', 'V-234567', '200 Tech Blvd', 'San Francisco', 'CA', '94101', 'USA', '415-555-2222', 'info@techsolutions.com', 'www.techsolutions.com', 'IT equipment vendor'),
(2, 'Furniture World', 'Furniture World Corp', 'V-345678', '300 Chair Ave', 'Seattle', 'WA', '98101', 'USA', '206-555-3333', 'info@furnitureworld.com', 'www.furnitureworld.com', 'Office furniture vendor'),
(2, 'Marketing Experts', 'Marketing Experts Co.', 'V-456789', '400 Ad St', 'Denver', 'CO', '80201', 'USA', '303-555-4444', 'info@marketingexperts.com', 'www.marketingexperts.com', 'Marketing services vendor'),
(2, 'Shipping Partners', 'Shipping Partners Inc.', 'V-567890', '500 Delivery Rd', 'Atlanta', 'GA', '30301', 'USA', '404-555-5555', 'info@shippingpartners.com', 'www.shippingpartners.com', 'Shipping services vendor'),

-- Employees
(3, 'David Miller', NULL, 'E-123456', '111 Worker St', 'Dallas', 'TX', '75201', 'USA', '214-555-6666', 'david@company.com', NULL, 'Sales Manager'),
(3, 'Jennifer Lee', NULL, 'E-234567', '222 Staff Ave', 'Phoenix', 'AZ', '85001', 'USA', '602-555-7777', 'jennifer@company.com', NULL, 'Accountant'),
(3, 'Thomas Clark', NULL, 'E-345678', '333 Employee Rd', 'Philadelphia', 'PA', '19101', 'USA', '215-555-8888', 'thomas@company.com', NULL, 'Operations Manager'),
(3, 'Amanda White', NULL, 'E-456789', '444 Team St', 'San Diego', 'CA', '92101', 'USA', '619-555-9999', 'amanda@company.com', NULL, 'Marketing Specialist'),
(3, 'James Taylor', NULL, 'E-567890', '555 Colleague Dr', 'Portland', 'OR', '97201', 'USA', '503-555-0000', 'james@company.com', NULL, 'IT Specialist');

-- Fiscal Years
INSERT INTO fiscal_years (name, start_date, end_date, is_closed) VALUES
('FY 2022', '2022-01-01', '2022-12-31', 0);

-- Currencies
INSERT INTO currencies (code, name, symbol, is_default) VALUES
('USD', 'US Dollar', '$', 1),
('EUR', 'Euro', '€', 0),
('GBP', 'British Pound', '£', 0),
('CAD', 'Canadian Dollar', 'C$', 0),
('JPY', 'Japanese Yen', '¥', 0);

-- Tax Rates
INSERT INTO tax_rates (name, rate, description) VALUES
('No Tax', 0.00, 'No tax applied'),
('Sales Tax', 7.50, 'Standard sales tax'),
('Reduced Tax', 3.50, 'Reduced rate for certain goods'),
('VAT Standard', 20.00, 'Standard VAT rate'),
('VAT Reduced', 10.00, 'Reduced VAT rate');

-- Payment Methods
INSERT INTO payment_methods (name) VALUES
('Cash'),
('Credit Card'),
('Bank Transfer'),
('Check'),
('PayPal'),
('Other');

-- Bank Accounts
INSERT INTO bank_accounts (account_id, bank_name, account_number, description, currency_id, opening_balance, current_balance) VALUES
(5, 'First National Bank', '1234567890', 'Main Checking Account', 1, 10000.00, 10000.00),
(6, 'First National Bank', '0987654321', 'Savings Account', 1, 25000.00, 25000.00),
(5, 'International Bank', 'EUR1234567', 'Euro Account', 2, 5000.00, 5000.00);
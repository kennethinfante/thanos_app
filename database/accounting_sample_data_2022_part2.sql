-- Product Categories
INSERT INTO product_categories (name, description) VALUES
('Electronics', 'Electronic devices and accessories'),
('Office Supplies', 'General office supplies'),
('Furniture', 'Office furniture and fixtures'),
('Software', 'Computer software and licenses'),
('Services', 'Professional services');

-- Products
INSERT INTO products (name, description, sku, category_id, sale_price, purchase_price, tax_rate_id, is_active, inventory_tracking, current_stock, reorder_level, inventory_account_id, revenue_account_id, expense_account_id) VALUES
('Laptop Computer', 'Business laptop', 'ELEC-001', 1, 1200.00, 900.00, 2, 1, 1, 15, 5, 8, 32, 37),
('Desktop Computer', 'Office desktop', 'ELEC-002', 1, 950.00, 700.00, 2, 1, 1, 10, 3, 8, 32, 37),
('Office Chair', 'Ergonomic office chair', 'FURN-001', 3, 250.00, 150.00, 2, 1, 1, 20, 5, 8, 32, 37),
('Office Desk', 'Standard office desk', 'FURN-002', 3, 350.00, 200.00, 2, 1, 1, 10, 3, 8, 32, 37),
('Printer Paper', 'Letter size paper, 500 sheets', 'SUPP-001', 2, 5.99, 3.50, 2, 1, 1, 100, 20, 8, 32, 37),
('Ink Cartridges', 'Black ink cartridges', 'SUPP-002', 2, 24.99, 15.00, 2, 1, 1, 30, 10, 8, 32, 37),
('Accounting Software', 'Annual license', 'SOFT-001', 4, 299.99, 299.99, 2, 1, 0, NULL, NULL, NULL, 32, 37),
('IT Support', 'Hourly IT support', 'SERV-001', 5, 75.00, 75.00, 2, 1, 0, NULL, NULL, NULL, 33, 37),
('Consulting Services', 'Business consulting, per hour', 'SERV-002', 5, 150.00, 150.00, 2, 1, 0, NULL, NULL, NULL, 33, 37),
('Smartphone', 'Business smartphone', 'ELEC-003', 1, 699.99, 500.00, 2, 1, 1, 8, 3, 8, 32, 37);

-- Journal Entries for 2022
INSERT INTO journal_entries (date, entry_number, description, notes, is_posted) VALUES
-- January 2022
('2022-01-05', 'JE-2022-001', 'Initial capital investment', 'Owner investment to start business operations', 1),
('2022-01-10', 'JE-2022-002', 'Office rent payment', 'Monthly office rent', 1),
('2022-01-15', 'JE-2022-003', 'Purchase of office supplies', 'Initial office supplies', 1),
('2022-01-20', 'JE-2022-004', 'Sales revenue', 'First sales of the year', 1),
('2022-01-25', 'JE-2022-005', 'Utility bills payment', 'Electricity and water bills', 1),
('2022-01-31', 'JE-2022-006', 'Payroll entry', 'January payroll', 1),

-- February 2022
('2022-02-05', 'JE-2022-007', 'Purchase of equipment', 'New computers for office', 1),
('2022-02-10', 'JE-2022-008', 'Office rent payment', 'Monthly office rent', 1),
('2022-02-15', 'JE-2022-009', 'Sales revenue', 'February sales', 1),
('2022-02-20', 'JE-2022-010', 'Marketing expenses', 'Online advertising campaign', 1),
('2022-02-25', 'JE-2022-011', 'Utility bills payment', 'Electricity and water bills', 1),
('2022-02-28', 'JE-2022-012', 'Payroll entry', 'February payroll', 1),

-- March 2022
('2022-03-05', 'JE-2022-013', 'Insurance payment', 'Annual business insurance', 1),
('2022-03-10', 'JE-2022-014', 'Office rent payment', 'Monthly office rent', 1),
('2022-03-15', 'JE-2022-015', 'Sales revenue', 'March sales', 1),
('2022-03-20', 'JE-2022-016', 'Purchase of inventory', 'Inventory restocking', 1),
('2022-03-25', 'JE-2022-017', 'Utility bills payment', 'Electricity and water bills', 1),
('2022-03-31', 'JE-2022-018', 'Payroll entry', 'March payroll', 1),

-- April 2022
('2022-04-05', 'JE-2022-019', 'Quarterly tax payment', 'Q1 tax payment', 1),
('2022-04-10', 'JE-2022-020', 'Office rent payment', 'Monthly office rent', 1),
('2022-04-15', 'JE-2022-021', 'Sales revenue', 'April sales', 1),
('2022-04-20', 'JE-2022-022', 'Software subscription', 'Annual software licenses', 1),
('2022-04-25', 'JE-2022-023', 'Utility bills payment', 'Electricity and water bills', 1),
('2022-04-30', 'JE-2022-024', 'Payroll entry', 'April payroll', 1),

-- May-December entries would follow the same pattern
-- Adding a few more for May
('2022-05-10', 'JE-2022-025', 'Office rent payment', 'Monthly office rent', 1),
('2022-05-15', 'JE-2022-026', 'Sales revenue', 'May sales', 1),
('2022-05-31', 'JE-2022-027', 'Payroll entry', 'May payroll', 1);

-- Journal Entry Lines for 2022 (sample for January-February)
INSERT INTO journal_entry_lines (journal_entry_id, account_id, description, debit, credit) VALUES
-- JE-2022-001: Initial capital investment
(1, 5, 'Cash investment', 50000.00, 0.00),
(1, 28, 'Owner capital', 0.00, 50000.00),

-- JE-2022-002: Office rent payment
(2, 39, 'Monthly office rent', 2000.00, 0.00),
(2, 5, 'Payment from checking account', 0.00, 2000.00),

-- JE-2022-003: Purchase of office supplies
(3, 41, 'Office supplies purchase', 500.00, 0.00),
(3, 5, 'Payment from checking account', 0.00, 500.00),

-- JE-2022-004: Sales revenue
(4, 5, 'Cash from sales', 7500.00, 0.00),
(4, 32, 'Revenue from product sales', 0.00, 7500.00),

-- JE-2022-005: Utility bills payment
(5, 40, 'Monthly utilities', 350.00, 0.00),
(5, 5, 'Payment from checking account', 0.00, 350.00),

-- JE-2022-006: Payroll entry
(6, 38, 'Monthly payroll', 12000.00, 0.00),
(6, 5, 'Payment from checking account', 0.00, 12000.00),

-- JE-2022-007: Purchase of equipment
(7, 11, 'New office computers', 5000.00, 0.00),
(7, 5, 'Payment from checking account', 0.00, 5000.00),

-- JE-2022-008: Office rent payment
(8, 39, 'Monthly office rent', 2000.00, 0.00),
(8, 5, 'Payment from checking account', 0.00, 2000.00);

-- Invoices for 2022 (sample)
INSERT INTO invoices (customer_id, invoice_number, date, due_date, total_amount, tax_amount, notes, status) VALUES
(1, 'INV-2022-001', '2022-01-15', '2022-02-14', 2675.00, 175.00, 'Computer equipment sale', 'paid'),
(2, 'INV-2022-002', '2022-01-20', '2022-02-19', 4815.00, 315.00, 'Office furniture purchase', 'paid'),
(3, 'INV-2022-003', '2022-02-05', '2022-03-07', 1070.00, 70.00, 'Software licenses', 'paid'),
(4, 'INV-2022-004', '2022-02-15', '2022-03-17', 3210.00, 210.00, 'IT consulting services', 'paid'),
(5, 'INV-2022-005', '2022-03-01', '2022-03-31', 5350.00, 350.00, 'Office equipment and supplies', 'paid'),
(1, 'INV-2022-006', '2022-03-15', '2022-04-14', 2140.00, 140.00, 'Computer accessories', 'paid'),
(2, 'INV-2022-007', '2022-04-01', '2022-05-01', 3745.00, 245.00, 'Office renovation services', 'paid'),
(3, 'INV-2022-008', '2022-04-15', '2022-05-15', 1605.00, 105.00, 'Software maintenance', 'paid');

-- Invoice Lines (sample)
INSERT INTO invoice_lines (invoice_id, product_id, description, quantity, unit_price, tax_rate_id, tax_amount, line_total) VALUES
(1, 1, 'Laptop Computer', 2, 1200.00, 2, 180.00, 2580.00),
(1, 6, 'Ink Cartridges', 4, 24.99, 2, 7.50, 107.46),
(2, 3, 'Office Chair', 10, 250.00, 2, 187.50, 2687.50),
(2, 4, 'Office Desk', 5, 350.00, 2, 131.25, 1881.25),
(3, 7, 'Accounting Software', 3, 299.99, 2, 67.50, 967.47),
(3, 5, 'Printer Paper', 20, 5.99, 2, 8.99, 128.79),
(4, 8, 'IT Support', 40, 75.00, 2, 225.00, 3225.00),
(5, 2, 'Desktop Computer', 5, 950.00, 2, 356.25, 5106.25),
(5, 6, 'Ink Cartridges', 10, 24.99, 2, 18.74, 268.64);

-- Bills for 2022 (sample)
-- Bills for 2022 (sample)
INSERT INTO bills (vendor_id, bill_number, date, due_date, total_amount, tax_amount, notes, status) VALUES
(6, 'BILL-2022-001', '2022-01-05', '2022-02-04', 535.00, 35.00, 'Office supplies purchase', 'paid'),
(7, 'BILL-2022-002', '2022-01-15', '2022-02-14', 3210.00, 210.00, 'IT equipment purchase', 'paid'),
(8, 'BILL-2022-003', '2022-02-01', '2022-03-03', 2140.00, 140.00, 'Office furniture purchase', 'paid'),
(9, 'BILL-2022-004', '2022-02-15', '2022-03-17', 1070.00, 70.00, 'Marketing services', 'paid'),
(10, 'BILL-2022-005', '2022-03-01', '2022-03-31', 428.00, 28.00, 'Office supplies restock', 'paid'),
(6, 'BILL-2022-006', '2022-03-15', '2022-04-14', 1605.00, 105.00, 'Computer accessories', 'paid'),
(7, 'BILL-2022-007', '2022-04-01', '2022-05-01', 2675.00, 175.00, 'Software licenses', 'paid'),
(8, 'BILL-2022-008', '2022-04-15', '2022-05-15', 3745.00, 245.00, 'Office renovation', 'paid');

-- Bill Lines (sample)
INSERT INTO bill_lines (bill_id, product_id, description, quantity, unit_price, tax_rate_id, tax_amount, line_total) VALUES
(1, 5, 'Printer Paper', 50, 5.99, 2, 22.46, 321.96),
(1, 6, 'Ink Cartridges', 8, 24.99, 2, 14.99, 214.91),
(2, 1, 'Laptop Computer', 2, 1200.00, 2, 180.00, 2580.00),
(2, 10, 'Smartphone', 1, 699.99, 2, 52.50, 752.49),
(3, 3, 'Office Chair', 5, 250.00, 2, 93.75, 1343.75),
(3, 4, 'Office Desk', 2, 350.00, 2, 52.50, 752.50),
(4, 9, 'Consulting Services', 7, 150.00, 2, 78.75, 1128.75),
(5, 5, 'Printer Paper', 40, 5.99, 2, 17.97, 257.57),
(5, 6, 'Ink Cartridges', 7, 24.99, 2, 13.12, 188.05);

-- Payments for 2022 (sample)
INSERT INTO invoice_payments (date, invoice_id, amount, reference, notes, payment_method_id) VALUES
('2022-01-20', 1, 2675.00, 'IP-2022-001', 'Payment for INV-2022-001', 3),
('2022-01-25', 2, 4815.00, 'IP-2022-002', 'Payment for INV-2022-002', 2),
('2022-02-10', 3, 1070.00, 'IP-2022-003', 'Payment for INV-2022-003', 3),
('2022-02-20', 4, 3210.00, 'IP-2022-004', 'Payment for INV-2022-004', 2),
('2022-03-05', 5, 5350.00, 'IP-2022-005', 'Payment for INV-2022-005', 3),
('2022-03-20', 1, 2140.00, 'IP-2022-006', 'Payment for INV-2022-006', 2),
('2022-04-05', 2, 3745.00, 'IP-2022-007', 'Payment for INV-2022-007', 3),
('2022-04-20', 3, 1605.00, 'IP-2022-008', 'Payment for INV-2022-008', 2);

-- Bill Payments for 2022 (sample)
INSERT INTO bill_payments (date, bill_id, amount, reference, notes, payment_method_id) VALUES
('2022-01-15', 1, 535.00, 'BP-2022-001', 'Payment for BILL-2022-001', 3),
('2022-01-25', 2, 3210.00, 'BP-2022-002', 'Payment for BILL-2022-002', 2),
('2022-02-10', 3, 2140.00, 'BP-2022-003', 'Payment for BILL-2022-003', 3),
('2022-02-25', 4, 1070.00, 'BP-2022-004', 'Payment for BILL-2022-004', 2),
('2022-03-10', 5, 428.00, 'BP-2022-005', 'Payment for BILL-2022-005', 3),
('2022-03-25', 6, 1605.00, 'BP-2022-006', 'Payment for BILL-2022-006', 2),
('2022-04-10', 7, 2675.00, 'BP-2022-007', 'Payment for BILL-2022-007', 3),
('2022-04-25', 8, 3745.00, 'BP-2022-008', 'Payment for BILL-2022-008', 2);

-- Bank Transactions for 2022 (sample)
INSERT INTO bank_transactions (bank_account_id, date, description, amount, type, is_reconciled, journal_entry_id, invoice_payment_id, bill_payment_id) VALUES
(1, '2022-01-05', 'Initial capital investment', 50000.00, 'deposit',  1, 1, NULL, NULL),
(1, '2022-01-10', 'Office rent payment', -2000.00, 'withdrawal',  1, 2, NULL, NULL),
(1, '2022-01-15', 'Purchase of office supplies', -500.00, 'withdrawal',  1, 3, NULL, NULL),
(1, '2022-01-15', 'Payment for BILL-2022-001', -535.00, 'withdrawal',  1, NULL, NULL, 1),
(1, '2022-01-20', 'Sales revenue', 7500.00, 'deposit',  1, 4, NULL, NULL),
(1, '2022-01-20', 'Payment received for INV-2022-001', 2675.00, 'deposit', 1, NULL, 1, NULL),
(1, '2022-01-25', 'Utility bills payment', -350.00, 'withdrawal',  1, 5, NULL, NULL),
(1, '2022-01-25', 'Payment for BILL-2022-002', -3210.00, 'withdrawal',  1, NULL, NULL, 2),
(1, '2022-01-25', 'Payment received for INV-2022-002', 4815.00, 'deposit', 1, NULL, 2, NULL),
(1, '2022-01-31', 'Payroll entry', -12000.00, 'withdrawal',  1, 6, NULL, NULL),
(1, '2022-02-05', 'Purchase of equipment', -5000.00, 'withdrawal',  1, 7, NULL, NULL),
(1, '2022-02-10', 'Office rent payment', -2000.00, 'withdrawal',  1, 8, NULL, NULL),
(1, '2022-02-10', 'Payment for BILL-2022-003', -2140.00, 'withdrawal',  1, NULL, NULL, 3),
(1, '2022-02-10', 'Payment received for INV-2022-003', 1070.00, 'deposit', 1, NULL, 3, NULL);

-- -- Financial Reports for 2022
-- INSERT INTO financial_reports (name, report_type, date_range_start, date_range_end, created_date, parameters) VALUES
-- ('Income Statement - Q1 2022', 'income_statement', '2022-01-01', '2022-03-31', '2022-04-05', '{"include_zero_balances": false}'),
-- ('Balance Sheet - Q1 2022', 'balance_sheet', '2022-01-01', '2022-03-31', '2022-04-05', '{"include_zero_balances": false}'),
-- ('Cash Flow Statement - Q1 2022', 'cash_flow', '2022-01-01', '2022-03-31', '2022-04-05', '{"include_zero_balances": false}'),
-- ('Income Statement - April 2022', 'income_statement', '2022-04-01', '2022-04-30', '2022-05-05', '{"include_zero_balances": false}'),
-- ('Balance Sheet - April 2022', 'balance_sheet', '2022-04-01', '2022-04-30', '2022-05-05', '{"include_zero_balances": false}'),
-- ('Cash Flow Statement - April 2022', 'cash_flow', '2022-04-01', '2022-04-30', '2022-05-05', '{"include_zero_balances": false}');
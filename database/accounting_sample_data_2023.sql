-- Sample Data for 2023

-- Fiscal Years
INSERT INTO fiscal_years (name, start_date, end_date, is_closed) VALUES
('FY 2023', '2023-01-01', '2023-12-31', 0);

-- Journal Entries for 2023
INSERT INTO journal_entries (date, reference, description, is_posted, notes) VALUES
-- January 2023
('2023-01-05', 'JE-2023-001', 'Annual planning adjustments', 1, 'Adjustments for new fiscal year'),
('2023-01-10', 'JE-2023-002', 'Office rent payment', 1, 'Monthly office rent'),
('2023-01-15', 'JE-2023-003', 'Purchase of office supplies', 1, 'Office supplies for Q1'),
('2023-01-20', 'JE-2023-004', 'Sales revenue', 1, 'First sales of the year'),
('2023-01-25', 'JE-2023-005', 'Utility bills payment', 1, 'Electricity and water bills'),
('2023-01-31', 'JE-2023-006', 'Payroll entry', 1, 'January payroll'),

-- February 2023
('2023-02-05', 'JE-2023-007', 'Technology upgrade', 1, 'New server and networking equipment'),
('2023-02-10', 'JE-2023-008', 'Office rent payment', 1, 'Monthly office rent'),
('2023-02-15', 'JE-2023-009', 'Sales revenue', 1, 'February sales'),
('2023-02-20', 'JE-2023-010', 'Digital marketing campaign', 1, 'Social media and SEO campaign'),
('2023-02-25', 'JE-2023-011', 'Utility bills payment', 1, 'Electricity and water bills'),
('2023-02-28', 'JE-2023-012', 'Payroll entry', 1, 'February payroll'),

-- March 2023
('2023-03-05', 'JE-2023-013', 'Insurance renewal', 1, 'Annual business insurance'),
('2023-03-10', 'JE-2023-014', 'Office rent payment', 1, 'Monthly office rent'),
('2023-03-15', 'JE-2023-015', 'Sales revenue', 1, 'March sales'),
('2023-03-20', 'JE-2023-016', 'Inventory purchase', 1, 'Q2 inventory stock'),
('2023-03-25', 'JE-2023-017', 'Utility bills payment', 1, 'Electricity and water bills'),
('2023-03-31', 'JE-2023-018', 'Payroll entry', 1, 'March payroll'),

-- April 2023
('2023-04-05', 'JE-2023-019', 'Quarterly tax payment', 1, 'Q1 tax payment'),
('2023-04-10', 'JE-2023-020', 'Office rent payment', 1, 'Monthly office rent'),
('2023-04-15', 'JE-2023-021', 'Sales revenue', 1, 'April sales'),
('2023-04-20', 'JE-2023-022', 'Software subscription renewal', 1, 'Annual software licenses'),
('2023-04-25', 'JE-2023-023', 'Utility bills payment', 1, 'Electricity and water bills'),
('2023-04-30', 'JE-2023-024', 'Payroll entry', 1, 'April payroll'),

-- May 2023
('2023-05-10', 'JE-2023-025', 'Office rent payment', 1, 'Monthly office rent'),
('2023-05-15', 'JE-2023-026', 'Sales revenue', 1, 'May sales'),
('2023-05-20', 'JE-2023-027', 'Office renovation', 1, 'Reception area update'),
('2023-05-25', 'JE-2023-028', 'Utility bills payment', 1, 'Electricity and water bills'),
('2023-05-31', 'JE-2023-029', 'Payroll entry', 1, 'May payroll');

-- Journal Entry Lines for 2023 (sample for January-February)
INSERT INTO journal_entry_lines (journal_entry_id, account_id, description, debit, credit) VALUES
-- JE-2023-001: Annual planning adjustments
(28, 11, 'Depreciation adjustment', 2500.00, 0.00),
(28, 24, 'Accumulated depreciation', 0.00, 2500.00),

-- JE-2023-002: Office rent payment
(29, 39, 'Monthly office rent', 2200.00, 0.00),
(29, 5, 'Payment from checking account', 0.00, 2200.00),

-- JE-2023-003: Purchase of office supplies
(30, 41, 'Office supplies purchase', 750.00, 0.00),
(30, 5, 'Payment from checking account', 0.00, 750.00),

-- JE-2023-004: Sales revenue
(31, 5, 'Cash from sales', 9500.00, 0.00),
(31, 32, 'Revenue from product sales', 0.00, 9500.00),

-- JE-2023-005: Utility bills payment
(32, 40, 'Monthly utilities', 425.00, 0.00),
(32, 5, 'Payment from checking account', 0.00, 425.00),

-- JE-2023-006: Payroll entry
(33, 38, 'Monthly payroll', 13500.00, 0.00),
(33, 5, 'Payment from checking account', 0.00, 13500.00),

-- JE-2023-007: Technology upgrade
(34, 11, 'Server and networking equipment', 8500.00, 0.00),
(34, 5, 'Payment from checking account', 0.00, 8500.00),

-- JE-2023-008: Office rent payment
(35, 39, 'Monthly office rent', 2200.00, 0.00),
(35, 5, 'Payment from checking account', 0.00, 2200.00);

-- Invoices for 2023 (sample)
INSERT INTO invoices (contact_id, invoice_number, date, due_date, status, total_amount, tax_amount, notes) VALUES
(1, 'INV-2023-001', '2023-01-15', '2023-02-14', 'paid', 3210.00, 210.00, 'Computer equipment sale'),
(2, 'INV-2023-002', '2023-01-25', '2023-02-24', 'paid', 5350.00, 350.00, 'Office furniture purchase'),
(3, 'INV-2023-003', '2023-02-05', '2023-03-07', 'paid', 1605.00, 105.00, 'Software licenses'),
(4, 'INV-2023-004', '2023-02-20', '2023-03-22', 'paid', 4280.00, 280.00, 'IT consulting services'),
(5, 'INV-2023-005', '2023-03-10', '2023-04-09', 'paid', 6420.00, 420.00, 'Office equipment and supplies'),
(1, 'INV-2023-006', '2023-03-25', '2023-04-24', 'paid', 2675.00, 175.00, 'Computer accessories'),
(2, 'INV-2023-007', '2023-04-05', '2023-05-05', 'paid', 4815.00, 315.00, 'Office renovation services'),
(3, 'INV-2023-008', '2023-04-20', '2023-05-20', 'paid', 2140.00, 140.00, 'Software maintenance'),
(4, 'INV-2023-009', '2023-05-10', '2023-06-09', 'unpaid', 3745.00, 245.00, 'IT infrastructure upgrade'),
(5, 'INV-2023-010', '2023-05-25', '2023-06-24', 'unpaid', 1070.00, 70.00, 'Office supplies');

-- Invoice Lines (sample)
INSERT INTO invoice_lines (invoice_id, product_id, description, quantity, unit_price, tax_rate_id, tax_amount, line_total) VALUES
(9, 1, 'Laptop Computer', 2, 1200.00, 2, 180.00, 2580.00),
(9, 10, 'Smartphone', 1, 699.99, 2, 52.50, 752.49),
(10, 3, 'Office Chair', 12, 250.00, 2, 225.00, 3225.00),
(10, 4, 'Office Desk', 6, 350.00, 2, 157.50, 2257.50),
(11, 7, 'Accounting Software', 5, 299.99, 2, 112.50, 1612.45),
(12, 8, 'IT Support', 55, 75.00, 2, 309.38, 4434.38),
(13, 2, 'Desktop Computer', 6, 950.00, 2, 427.50, 6127.50),
(13, 6, 'Ink Cartridges', 12, 24.99, 2, 22.49, 322.37),
(14, 1, 'Laptop Computer', 2, 1200.00, 2, 180.00, 2580.00),
(14, 5, 'Printer Paper', 20, 5.99, 2, 8.99, 128.79),
(15, 3, 'Office Chair', 10, 250.00, 2, 187.50, 2687.50),
(15, 4, 'Office Desk', 6, 350.00, 2, 157.50, 2257.50),
(16, 7, 'Accounting Software', 7, 299.99, 2, 157.49, 2257.42),
(17, 9, 'Consulting Services', 25, 150.00, 2, 281.25, 4031.25),
(18, 6, 'Ink Cartridges', 40, 24.99, 2, 74.97, 1074.57);

-- Bills for 2023 (sample)
INSERT INTO bills (contact_id, bill_number, date, due_date, status, total_amount, tax_amount, notes) VALUES
(6, 'BILL-2023-001', '2023-01-10', '2023-02-09', 'paid', 1070.00, 70.00, 'Office supplies purchase'),
(7, 'BILL-2023-002', '2023-01-20', '2023-02-19', 'paid', 4280.00, 280.00, 'IT equipment purchase'),
(8, 'BILL-2023-003', '2023-02-05', '2023-03-07', 'paid', 3210.00, 210.00, 'Office furniture purchase'),
(9, 'BILL-2023-004', '2023-02-25', '2023-03-27', 'paid', 2140.00, 140.00, 'Marketing services'),
(10, 'BILL-2023-005', '2023-03-10', '2023-04-09', 'paid', 856.00, 56.00, 'Office supplies restock'),
(6, 'BILL-2023-006', '2023-03-25', '2023-04-24', 'paid', 2675.00, 175.00, 'Computer accessories'),
(7, 'BILL-2023-007', '2023-04-10', '2023-05-10', 'paid', 3745.00, 245.00, 'Software licenses'),
(8, 'BILL-2023-008', '2023-04-25', '2023-05-25', 'paid', 5350.00, 350.00, 'Office renovation'),
(9, 'BILL-2023-009', '2023-05-15', '2023-06-14', 'unpaid', 1605.00, 105.00, 'Marketing campaign'),
(10, 'BILL-2023-010', '2023-05-30', '2023-06-29', 'unpaid', 4815.00, 315.00, 'Inventory purchase');

-- Bill Lines (sample)
INSERT INTO bill_lines (bill_id, product_id, description, quantity, unit_price, tax_rate_id, tax_amount, line_total) VALUES
(9, 5, 'Printer Paper', 100, 5.99, 2, 44.93, 643.93),
(9, 6, 'Ink Cartridges', 17, 24.99, 2, 31.86, 456.69),
(10, 1, 'Laptop Computer', 3, 1200.00, 2, 270.00, 3870.00),
(10, 10, 'Smartphone', 1, 699.99, 2, 52.50, 752.49),
(11, 3, 'Office Chair', 8, 250.00, 2, 150.00, 2150.00),
(11, 4, 'Office Desk', 3, 350.00, 2, 78.75, 1128.75),
(12, 9, 'Consulting Services', 14, 150.00, 2, 157.50, 2257.50),
(13, 5, 'Printer Paper', 80, 5.99, 2, 35.94, 515.14),
(13, 6, 'Ink Cartridges', 14, 24.99, 2, 26.24, 375.86),
(14, 1, 'Laptop Computer', 2, 1200.00, 2, 180.00, 2580.00),
(14, 5, 'Printer Paper', 20, 5.99, 2, 8.99, 128.79),
(15, 7, 'Accounting Software', 12, 299.99, 2, 270.00, 3869.88),
(16, 8, 'IT Support', 25, 150.00, 2, 281.25, 4031.25),
(17, 3, 'Office Chair', 12, 250.00, 2, 225.00, 3225.00),
(17, 4, 'Office Desk', 6, 350.00, 2, 157.50, 2257.50),
(18, 9, 'Consulting Services', 10, 150.00, 2, 112.50, 1612.50),
(18, 5, 'Printer Paper', 80, 5.99, 2, 35.94, 515.14);

-- Payments for 2023 (sample)
INSERT INTO payments (date, contact_id, amount, payment_method_id, reference, notes) VALUES
('2023-01-20', 1, 3210.00, 3, 'PAY-2023-001', 'Payment for INV-2023-001'),
('2023-01-30', 2, 5350.00, 2, 'PAY-2023-002', 'Payment for INV-2023-002'),
('2023-02-15', 3, 1605.00, 3, 'PAY-2023-003', 'Payment for INV-2023-003'),
('2023-02-28', 4, 4280.00, 2, 'PAY-2023-004', 'Payment for INV-2023-004'),
('2023-03-15', 5, 6420.00, 3, 'PAY-2023-005', 'Payment for INV-2023-005'),
('2023-03-30', 1, 2675.00, 2, 'PAY-2023-006', 'Payment for INV-2023-006'),
('2023-04-15', 2, 4815.00, 3, 'PAY-2023-007', 'Payment for INV-2023-007'),
('2023-04-30', 3, 2140.00, 2, 'PAY-2023-008', 'Payment for INV-2023-008');

-- Bill Payments for 2023 (sample)
INSERT INTO bill_payments (date, bill_id, amount, payment_method_id, reference, notes) VALUES
('2023-01-20', 9, 1070.00, 3, 'BP-2023-001', 'Payment for BILL-2023-001'),
('2023-01-30', 10, 4280.00, 2, 'BP-2023-002', 'Payment for BILL-2023-002'),
('2023-02-15', 11, 3210.00, 3, 'BP-2023-003', 'Payment for BILL-2023-003'),
('2023-02-28', 12, 2140.00, 2, 'BP-2023-004', 'Payment for BILL-2023-004'),
('2023-03-15', 13, 856.00, 3, 'BP-2023-005', 'Payment for BILL-2023-005'),
('2023-03-30', 14, 2675.00, 2, 'BP-2023-006', 'Payment for BILL-2023-006'),
('2023-04-15', 15, 3745.00, 3, 'BP-2023-007', 'Payment for BILL-2023-007'),
('2023-04-30', 16, 5350.00, 2, 'BP-2023-008', 'Payment for BILL-2023-008');

-- Bank Transactions for 2023 (sample)
INSERT INTO bank_transactions (bank_account_id, date, description, amount, type, reference, reconciled) VALUES
(1, '2023-01-05', 'Beginning balance for 2023', 75000.00, 'deposit', 'JE-2023-001', 1),
(1, '2023-01-10', 'Office rent payment', -2200.00, 'withdrawal', 'JE-2023-002', 1),
(1, '2023-01-15', 'Purchase of office supplies', -750.00, 'withdrawal', 'JE-2023-003', 1),
(1, '2023-01-15', 'Payment for BILL-2023-001', -1070.00, 'withdrawal', 'BP-2023-001', 1),
(1, '2023-01-20', 'Sales revenue', 9500.00, 'deposit', 'JE-2023-004', 1),
(1, '2023-01-20', 'Payment received for INV-2023-001', 3210.00, 'deposit', 'PAY-2023-001', 1),
(1, '2023-01-25', 'Utility bills payment', -425.00, 'withdrawal', 'JE-2023-005', 1),
(1, '2023-01-30', 'Payment for BILL-2023-002', -4280.00, 'withdrawal', 'BP-2023-002', 1),
(1, '2023-01-30', 'Payment received for INV-2023-002', 5350.00, 'deposit', 'PAY-2023-002', 1),
(1, '2023-01-31', 'Payroll entry', -13500.00, 'withdrawal', 'JE-2023-006', 1),
(1, '2023-02-05', 'Technology upgrade', -8500.00, 'withdrawal', 'JE-2023-007', 1),
(1, '2023-02-10', 'Office rent payment', -2200.00, 'withdrawal', 'JE-2023-008', 1),
(1, '2023-02-15', 'Payment for BILL-2023-003', -3210.00, 'withdrawal', 'BP-2023-003', 1),
(1, '2023-02-15', 'Payment received for INV-2023-003', 1605.00, 'deposit', 'PAY-2023-003', 1),
(1, '2023-02-20', 'Digital marketing campaign', -1500.00, 'withdrawal', 'JE-2023-010', 1),
(1, '2023-02-25', 'Utility bills payment', -450.00, 'withdrawal', 'JE-2023-011', 1),
(1, '2023-02-28', 'Payment for BILL-2023-004', -2140.00, 'withdrawal', 'BP-2023-004', 1),
(1, '2023-02-28', 'Payment received for INV-2023-004', 4280.00, 'deposit', 'PAY-2023-004', 1),
(1, '2023-02-28', 'Payroll entry', -13500.00, 'withdrawal', 'JE-2023-012', 1);

-- Financial Reports for 2023
INSERT INTO financial_reports (name, report_type, date_range_start, date_range_end, created_date, parameters) VALUES
('Income Statement - Q1 2023', 'income_statement', '2023-01-01', '2023-03-31', '2023-04-05', '{"include_zero_balances": false}'),
('Balance Sheet - Q1 2023', 'balance_sheet', '2023-01-01', '2023-03-31', '2023-04-05', '{"include_zero_balances": false}'),
('Cash Flow Statement - Q1 2023', 'cash_flow', '2023-01-01', '2023-03-31', '2023-04-05', '{"include_zero_balances": false}'),
('Income Statement - April 2023', 'income_statement', '2023-04-01', '2023-04-30', '2023-05-05', '{"include_zero_balances": false}'),
('Balance Sheet - April 2023', 'balance_sheet', '2023-04-01', '2023-04-30', '2023-05-05', '{"include_zero_balances": false}'),
('Cash Flow Statement - April 2023', 'cash_flow', '2023-04-01', '2023-04-30', '2023-05-05', '{"include_zero_balances": false}'),
('Income Statement - May 2023', 'income_statement', '2023-05-01', '2023-05-31', '2023-06-05', '{"include_zero_balances": false}'),
('Balance Sheet - May 2023', 'balance_sheet', '2023-05-01', '2023-05-31', '2023-06-05', '{"include_zero_balances": false}'),
('Cash Flow Statement - May 2023', 'cash_flow', '2023-05-01', '2023-05-31', '2023-06-05', '{"include_zero_balances": false}');

-- Budget entries for 2023
INSERT INTO budgets (fiscal_year_id, name, description) VALUES
(2, 'Operating Budget 2023', 'Main operating budget for fiscal year 2023'),
(2, 'Capital Expenditure Budget 2023', 'Budget for major purchases and investments in 2023'),
(2, 'Marketing Budget 2023', 'Budget allocated for marketing activities in 2023');

-- Budget Lines for 2023
INSERT INTO budget_lines (budget_id, account_id, period, amount) VALUES
-- Operating Budget 2023
(3, 32, '2023-01', 10000.00),  -- Revenue
(3, 32, '2023-02', 12000.00),  -- Revenue
(3, 32, '2023-03', 15000.00),  -- Revenue
(3, 32, '2023-04', 15000.00),  -- Revenue
(3, 32, '2023-05', 18000.00),  -- Revenue
(3, 32, '2023-06', 20000.00),  -- Revenue
(3, 38, '2023-01', 13000.00),  -- Payroll
(3, 38, '2023-02', 13000.00),  -- Payroll
(3, 38, '2023-03', 13500.00),  -- Payroll
(3, 38, '2023-04', 13500.00),  -- Payroll
(3, 38, '2023-05', 14000.00),  -- Payroll
(3, 38, '2023-06', 14000.00),  -- Payroll
(3, 39, '2023-01', 2200.00),   -- Rent
(3, 39, '2023-02', 2200.00),   -- Rent
(3, 39, '2023-03', 2200.00),   -- Rent
(3, 39, '2023-04', 2200.00),   -- Rent
(3, 39, '2023-05', 2200.00),   -- Rent
(3, 39, '2023-06', 2200.00),   -- Rent
(3, 40, '2023-01', 450.00),    -- Utilities
(3, 40, '2023-02', 450.00),    -- Utilities
(3, 40, '2023-03', 475.00),    -- Utilities
(3, 40, '2023-04', 475.00),    -- Utilities
(3, 40, '2023-05', 500.00),    -- Utilities
(3, 40, '2023-06', 500.00),    -- Utilities

-- Capital Expenditure Budget 2023
(4, 11, '2023-01', 0.00),      -- Equipment
(4, 11, '2023-02', 8500.00),   -- Equipment
(4, 11, '2023-03', 0.00),      -- Equipment
(4, 11, '2023-04', 0.00),      -- Equipment
(4, 11, '2023-05', 5000.00),   -- Equipment
(4, 11, '2023-06', 0.00),      -- Equipment
(4, 12, '2023-01', 0.00),      -- Furniture
(4, 12, '2023-02', 0.00),      -- Furniture
(4, 12, '2023-03', 0.00),      -- Furniture
(4, 12, '2023-04', 0.00),      -- Furniture
(4, 12, '2023-05', 3500.00),   -- Furniture
(4, 12, '2023-06', 0.00),      -- Furniture

-- Marketing Budget 2023
(5, 42, '2023-01', 500.00),    -- Marketing
(5, 42, '2023-02', 1500.00),   -- Marketing
(5, 42, '2023-03', 500.00),    -- Marketing
(5, 42, '2023-04', 500.00),    -- Marketing
(5, 42, '2023-05', 1500.00),   -- Marketing
(5, 42, '2023-06', 500.00);    -- Marketing

-- Tax Payments for 2023
INSERT INTO tax_payments (tax_rate_id, date, amount, reference, description) VALUES
(1, '2023-04-05', 4250.00, 'TAX-2023-Q1', 'Q1 2023 Sales Tax Payment'),
(2, '2023-04-05', 2850.00, 'TAX-2023-Q1-VAT', 'Q1 2023 VAT Payment');

-- Recurring Templates for 2023
INSERT INTO recurring_templates (name, type, frequency, start_date, end_date, next_due_date, description, template_data) VALUES
('Monthly Rent', 'bill', 'monthly', '2023-01-01', '2023-12-31', '2023-06-10', 'Monthly office rent payment', 
'{"contact_id": 6, "bill_number_prefix": "RENT-", "amount": 2200.00, "account_id": 39, "description": "Monthly Office Rent"}'),

('Monthly Utilities', 'bill', 'monthly', '2023-01-01', '2023-12-31', '2023-06-25', 'Monthly utility bills', 
'{"contact_id": 10, "bill_number_prefix": "UTIL-", "amount": 500.00, "account_id": 40, "description": "Monthly Utilities"}'),

('Monthly Payroll', 'journal_entry', 'monthly', '2023-01-01', '2023-12-31', '2023-06-30', 'Monthly payroll entry', 
'{"reference_prefix": "PAY-", "lines": [{"account_id": 38, "description": "Monthly Payroll", "debit": 14000.00}, {"account_id": 5, "description": "Payment from checking account", "credit": 14000.00}]}'),

('Quarterly Tax Payment', 'payment', 'quarterly', '2023-01-01', '2023-12-31', '2023-07-05', 'Quarterly tax payments', 
'{"payment_method_id": 2, "reference_prefix": "TAX-Q", "description": "Quarterly Tax Payment"}');

-- Document attachments for 2023 (metadata only)
INSERT INTO document_attachments (entity_type, entity_id, file_name, file_path, file_size, file_type, upload_date, description) VALUES
('invoice', 9, 'INV-2023-001.pdf', '/uploads/invoices/INV-2023-001.pdf', 125500, 'application/pdf', '2023-01-15', 'Invoice PDF'),
('bill', 9, 'BILL-2023-001.pdf', '/uploads/bills/BILL-2023-001.pdf', 98240, 'application/pdf', '2023-01-10', 'Bill PDF'),
('journal_entry', 28, 'JE-2023-001.xlsx', '/uploads/journal_entries/JE-2023-001.xlsx', 28500, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', '2023-01-05', 'Supporting calculations'),
('tax_payment', 1, 'TAX-2023-Q1.pdf', '/uploads/tax/TAX-2023-Q1.pdf', 145200, 'application/pdf', '2023-04-05', 'Q1 tax payment receipt');

-- User activity logs for 2023 (sample)
INSERT INTO activity_logs (user_id, action, entity_type, entity_id, details, timestamp) VALUES
(1, 'create', 'journal_entry', 28, '{"reference": "JE-2023-001", "description": "Annual planning adjustments"}', '2023-01-05 09:15:22'),
(1, 'create', 'invoice', 9, '{"invoice_number": "INV-2023-001", "total_amount": 3210.00}', '2023-01-15 11:30:45'),
(1, 'create', 'bill', 9, '{"bill_number": "BILL-2023-001", "total_amount": 1070.00}', '2023-01-10 14:22:18'),
(1, 'update', 'invoice', 9, '{"status": "paid", "previous_status": "draft"}', '2023-01-20 16:05:33'),
(1, 'create', 'payment', 1, '{"amount": 3210.00, "reference": "PAY-2023-001"}', '2023-01-20 16:10:12'),
(1, 'create', 'financial_report', 1, '{"name": "Income Statement - Q1 2023", "report_type": "income_statement"}', '2023-04-05 10:45:22'),
(1, 'create', 'tax_payment', 1, '{"amount": 4250.00, "reference": "TAX-2023-Q1"}', '2023-04-05 11:30:15'),
(1, 'create', 'budget', 3, '{"name": "Operating Budget 2023"}', '2023-01-03 13:20:45');

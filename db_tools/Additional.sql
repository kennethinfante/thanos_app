-- not yet run
-- Update some account balances to reflect Q2 2025 activity
UPDATE accounts SET current_balance = current_balance + 5000 WHERE id = 5; -- Increase in checking account
UPDATE accounts SET current_balance = current_balance + 3000 WHERE id = 7; -- Increase in accounts receivable
UPDATE accounts SET current_balance = current_balance - 2000 WHERE id = 19; -- Decrease in accounts payable
UPDATE accounts SET current_balance = current_balance + 8000 WHERE id = 32; -- Increase in revenue
UPDATE accounts SET current_balance = current_balance + 4000 WHERE id = 37; -- Increase in expenses

-- Update some account balances to reflect Q3 2025 activity
UPDATE accounts SET current_balance = current_balance + 7000 WHERE id = 5; -- Increase in checking account
UPDATE accounts SET current_balance = current_balance + 4000 WHERE id = 7; -- Increase in accounts receivable
UPDATE accounts SET current_balance = current_balance - 2500 WHERE id = 19; -- Decrease in accounts payable
UPDATE accounts SET current_balance = current_balance + 10000 WHERE id = 32; -- Increase in revenue
UPDATE accounts SET current_balance = current_balance + 5500 WHERE id = 37; -- Increase in expenses

-- Update some account balances to reflect Q4 2025 activity
UPDATE accounts SET current_balance = current_balance + 10000 WHERE id = 5; -- Increase in checking account
UPDATE accounts SET current_balance = current_balance + 5000 WHERE id = 7; -- Increase in accounts receivable
UPDATE accounts SET current_balance = current_balance - 3000 WHERE id = 19; -- Decrease in accounts payable
UPDATE accounts SET current_balance = current_balance + 15000 WHERE id = 32; -- Increase in revenue
UPDATE accounts SET current_balance = current_balance + 8000 WHERE id = 37; -- Increase in expenses

-- Close the fiscal year 2025
UPDATE fiscal_years SET is_closed = 1 WHERE name = 'FY 2025';

-- Update some account balances to reflect Q1 2026 activity
UPDATE accounts SET current_balance = current_balance + 12000 WHERE id = 5; -- Increase in checking account
UPDATE accounts SET current_balance = current_balance + 6000 WHERE id = 7; -- Increase in accounts receivable
UPDATE accounts SET current_balance = current_balance - 3500 WHERE id = 19; -- Decrease in accounts payable
UPDATE accounts SET current_balance = current_balance + 18000 WHERE id = 32; -- Increase in revenue
UPDATE accounts SET current_balance = current_balance + 9000 WHERE id = 37; -- Increase in expenses

-- Update some account balances to reflect Q2 2026 activity
UPDATE accounts SET current_balance = current_balance + 15000 WHERE id = 5; -- Increase in checking account
UPDATE accounts SET current_balance = current_balance + 7000 WHERE id = 7; -- Increase in accounts receivable
UPDATE accounts SET current_balance = current_balance - 4000 WHERE id = 19; -- Decrease in accounts payable
UPDATE accounts SET current_balance = current_balance + 22000 WHERE id = 32; -- Increase in revenue
UPDATE accounts SET current_balance = current_balance + 11000 WHERE id = 37; -- Increase in expenses
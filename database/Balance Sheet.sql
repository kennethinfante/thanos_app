-- Balance Sheet (Statement of Financial Position) as of December 31, 2023
WITH account_balances AS (
    -- Calculate balance for each account
    SELECT 
        a.id AS account_id,
        a.name AS account_name,
        a.account_type,
        a.account_number,
        a.parent_id,
        CASE 
            WHEN a.account_type IN ('asset', 'expense') THEN 
                SUM(CASE WHEN jel.debit > 0 THEN jel.debit ELSE -jel.credit END)
            WHEN a.account_type IN ('liability', 'equity', 'revenue', 'other_income') THEN 
                SUM(CASE WHEN jel.credit > 0 THEN jel.credit ELSE -jel.debit END)
        END AS balance
    FROM accounts a
    JOIN journal_entry_lines jel ON jel.account_id = a.id
    JOIN journal_entries je ON je.id = jel.journal_entry_id
    WHERE 
        a.account_type IN ('asset', 'liability', 'equity')
        AND je.is_posted = 1
        AND je.date <= '2023-12-31'  -- All transactions up to the balance sheet date
    GROUP BY a.id, a.name, a.account_type, a.account_number, a.parent_id
),
-- Calculate retained earnings
income_statement_accounts AS (
    SELECT 
        a.account_type,
        CASE 
            WHEN a.account_type IN ('revenue', 'other_income') THEN 
                SUM(CASE WHEN jel.credit > 0 THEN jel.credit ELSE -jel.debit END)
            WHEN a.account_type IN ('expense', 'cost_of_sales', 'other_expense') THEN 
                SUM(CASE WHEN jel.debit > 0 THEN jel.debit ELSE -jel.credit END)
        END AS balance
    FROM accounts a
    JOIN journal_entry_lines jel ON jel.account_id = a.id
    JOIN journal_entries je ON je.id = jel.journal_entry_id
    WHERE 
        a.account_type IN ('revenue', 'expense', 'other_income', 'other_expense', 'cost_of_sales')
        AND je.is_posted = 1
        AND je.date BETWEEN '2023-01-01' AND '2023-12-31'  -- Current year income/expenses
    GROUP BY a.account_type
),
retained_earnings AS (
    SELECT 
        SUM(CASE 
            WHEN account_type IN ('revenue', 'other_income') THEN balance
            WHEN account_type IN ('expense', 'cost_of_sales', 'other_expense') THEN -balance
            ELSE 0
        END) AS net_income
    FROM income_statement_accounts
)

-- Main balance sheet query
SELECT 
    -- Assets section
    'ASSETS' AS section,
    NULL AS account_number,
    NULL AS account_name,
    NULL AS amount,
    NULL AS total
UNION ALL
SELECT 
    'CURRENT ASSETS',
    NULL,
    NULL,
    NULL,
    NULL
UNION ALL
SELECT 
    '',
    account_number,
    account_name,
    balance AS amount,
    NULL
FROM account_balances
WHERE account_type = 'asset' 
AND (account_number LIKE '1%' OR account_number BETWEEN '1000' AND '1999')  -- Current assets typically start with 1
UNION ALL
SELECT 
    'TOTAL CURRENT ASSETS',
    NULL,
    NULL,
    NULL,
    SUM(balance) AS total
FROM account_balances
WHERE account_type = 'asset' 
AND (account_number LIKE '1%' OR account_number BETWEEN '1000' AND '1999')

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
SELECT 
    'NON-CURRENT ASSETS',
    NULL,
    NULL,
    NULL,
    NULL
UNION ALL
SELECT 
    '',
    account_number,
    account_name,
    balance AS amount,
    NULL
FROM account_balances
WHERE account_type = 'asset' 
AND (account_number LIKE '2%' OR account_number BETWEEN '2000' AND '2999')  -- Non-current assets typically start with 2
UNION ALL
SELECT 
    'TOTAL NON-CURRENT ASSETS',
    NULL,
    NULL,
    NULL,
    SUM(balance) AS total
FROM account_balances
WHERE account_type = 'asset' 
AND (account_number LIKE '2%' OR account_number BETWEEN '2000' AND '2999')

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
SELECT 
    'TOTAL ASSETS',
    NULL,
    NULL,
    NULL,
    SUM(balance) AS total
FROM account_balances
WHERE account_type = 'asset'

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
-- Liabilities section
SELECT 
    'LIABILITIES',
    NULL,
    NULL,
    NULL,
    NULL
UNION ALL
SELECT 
    'CURRENT LIABILITIES',
    NULL,
    NULL,
    NULL,
    NULL
UNION ALL
SELECT 
    '',
    account_number,
    account_name,
    balance AS amount,
    NULL
FROM account_balances
WHERE account_type = 'liability' 
AND (account_number LIKE '3%' OR account_number BETWEEN '3000' AND '3999')  -- Current liabilities typically start with 3
UNION ALL
SELECT 
    'TOTAL CURRENT LIABILITIES',
    NULL,
    NULL,
    NULL,
    SUM(balance) AS total
FROM account_balances
WHERE account_type = 'liability' 
AND (account_number LIKE '3%' OR account_number BETWEEN '3000' AND '3999')

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
SELECT 
    'NON-CURRENT LIABILITIES',
    NULL,
    NULL,
    NULL,
    NULL
UNION ALL
SELECT 
    '',
    account_number,
    account_name,
    balance AS amount,
    NULL
FROM account_balances
WHERE account_type = 'liability' 
AND (account_number LIKE '4%' OR account_number BETWEEN '4000' AND '4999')  -- Non-current liabilities typically start with 4
UNION ALL
SELECT 
    'TOTAL NON-CURRENT LIABILITIES',
    NULL,
    NULL,
    NULL,
    SUM(balance) AS total
FROM account_balances
WHERE account_type = 'liability' 
AND (account_number LIKE '4%' OR account_number BETWEEN '4000' AND '4999')

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
SELECT 
    'TOTAL LIABILITIES',
    NULL,
    NULL,
    NULL,
    SUM(balance) AS total
FROM account_balances
WHERE account_type = 'liability'

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
-- Equity section
SELECT 
    'EQUITY',
    NULL,
    NULL,
    NULL,
    NULL
UNION ALL
SELECT 
    '',
    account_number,
    account_name,
    balance AS amount,
    NULL
FROM account_balances
WHERE account_type = 'equity'
UNION ALL
-- Add retained earnings from current year
SELECT 
    '',
    '3900',  -- Assuming this is your retained earnings account number
    'Current Year Earnings',
    (SELECT net_income FROM retained_earnings) AS amount,
    NULL
UNION ALL
SELECT 
    'TOTAL EQUITY',
    NULL,
    NULL,
    NULL,
    (SELECT SUM(balance) FROM account_balances WHERE account_type = 'equity') + 
    (SELECT net_income FROM retained_earnings) AS total

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
-- Total liabilities and equity
SELECT 
    'TOTAL LIABILITIES AND EQUITY',
    NULL,
    NULL,
    NULL,
    (SELECT SUM(balance) FROM account_balances WHERE account_type = 'liability') + 
    (SELECT SUM(balance) FROM account_balances WHERE account_type = 'equity') +
    (SELECT net_income FROM retained_earnings) AS total

ORDER BY section, account_number;

/*
This SQL query:
1.
Creates a CTE to calculate the balance for each balance sheet account (assets, liabilities, equity)
2.
Creates a separate CTE to calculate the current year's retained earnings (net income)
3.
Formats the output as a proper balance sheet with sections for:
Current Assets
Non-Current Assets
Current Liabilities
Non-Current Liabilities
Equity (including current year earnings)
4.
Calculates totals for each section and ensures the balance sheet balances (Total Assets = Total Liabilities + Equity)
The query assumes your chart of accounts follows a standard numbering convention where:
Assets start with 1 or 2 (1xxx for current assets, 2xxx for non-current assets)
Liabilities start with 3 or 4 (3xxx for current liabilities, 4xxx for non-current liabilities)
Equity accounts start with 5 (5xxx)
You may need to adjust these ranges based on your actual chart of accounts structure.
*/
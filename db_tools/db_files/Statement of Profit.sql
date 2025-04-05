-- Income Statement (Statement of Profit and Loss) for 2023
WITH account_balances AS (
    -- Get all journal entry lines for income statement accounts
    SELECT 
        a.id AS account_id,
        a.name AS account_name,
        a.account_type AS account_type,
        a.account_number,
        a.parent_id,
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
        AND je.date BETWEEN '2023-01-01' AND '2023-12-31'
    GROUP BY a.id, a.name, a.account_type, a.account_number, a.parent_id
)

SELECT 
    -- Revenue section
    'REVENUE' AS section,
    NULL AS account_number,
    NULL AS account_name,
    NULL AS amount,
    NULL AS total
UNION ALL
SELECT 
    '',
    account_number,
    account_name,
    balance AS amount,
    NULL
FROM account_balances
WHERE account_type = 'revenue'
UNION ALL
SELECT 
    'TOTAL REVENUE',
    NULL,
    NULL,
    NULL,
    SUM(balance) AS total
FROM account_balances
WHERE account_type = 'revenue'

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
-- Cost of Sales section
SELECT 
    'COST OF SALES',
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
WHERE account_type = 'cost_of_sales'
UNION ALL
SELECT 
    'TOTAL COST OF SALES',
    NULL,
    NULL,
    NULL,
    SUM(balance) AS total
FROM account_balances
WHERE account_type = 'cost_of_sales'

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
-- Gross Profit calculation
SELECT 
    'GROSS PROFIT',
    NULL,
    NULL,
    NULL,
    (SELECT SUM(balance) FROM account_balances WHERE account_type = 'revenue') - 
    (SELECT COALESCE(SUM(balance), 0) FROM account_balances WHERE account_type = 'cost_of_sales')

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
-- Expenses section
SELECT 
    'EXPENSES',
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
WHERE account_type = 'expense'
UNION ALL
SELECT 
    'TOTAL EXPENSES',
    NULL,
    NULL,
    NULL,
    SUM(balance) AS total
FROM account_balances
WHERE account_type = 'expense'

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
-- Other Income section
SELECT 
    'OTHER INCOME',
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
WHERE account_type = 'other_income'
UNION ALL
SELECT 
    'TOTAL OTHER INCOME',
    NULL,
    NULL,
    NULL,
    COALESCE(SUM(balance), 0) AS total
FROM account_balances
WHERE account_type = 'other_income'

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
-- Other Expenses section
SELECT 
    'OTHER EXPENSES',
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
WHERE account_type = 'other_expense'
UNION ALL
SELECT 
    'TOTAL OTHER EXPENSES',
    NULL,
    NULL,
    NULL,
    COALESCE(SUM(balance), 0) AS total
FROM account_balances
WHERE account_type = 'other_expense'

UNION ALL
SELECT '','','','','' -- Empty row as separator

UNION ALL
-- Net Income calculation
SELECT 
    'NET INCOME',
    NULL,
    NULL,
    NULL,
    (SELECT SUM(balance) FROM account_balances WHERE account_type IN ('revenue', 'other_income')) - 
    (SELECT SUM(balance) FROM account_balances WHERE account_type IN ('expense', 'cost_of_sales', 'other_expense'))

ORDER BY section, account_number;

/*
This SQL query:
1.
Creates a CTE (Common Table Expression) to calculate the balance for each account
2.
Groups accounts by their type (revenue, expense, cost of sales, other income, other expense)
3.
Formats the output as a proper income statement with sections and totals
4.
Calculates gross profit and net income
You can run this query against your database to generate a complete income statement for the 2023 fiscal year. You can also modify the date range in the WHERE clause to generate statements for different periods.
*/

-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV

SELECT
    amfi_code,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;


-- 3. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 4. Funds with Expense Ratio < 1%

SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 5. Average Transaction Amount

SELECT
    transaction_type,
    AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 6. Top 5 States by Total Investment Amount

SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 5;


-- 7. Total Redemption Amount

SELECT
    SUM(amount_inr) AS total_redemption
FROM fact_transactions
WHERE transaction_type = 'Redemption';


-- 8. Top 5 Funds by 5-Year Return

SELECT
    amfi_code,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;


-- 9. Number of Funds by Risk Category

SELECT
    risk_grade,
    COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;


-- 10. Average Expense Ratio

SELECT
    AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance;
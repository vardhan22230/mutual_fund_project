
Mutual Fund Analytics Data Dictionary

 1. Fund Master Dataset

| Column Name        | Data Type | Description                      |
| ------------------ | --------- | -------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier    |
| fund_house         | Text      | Mutual fund company name         |
| scheme_name        | Text      | Name of the scheme               |
| category           | Text      | Fund category (Equity/Debt)      |
| sub_category       | Text      | Detailed category classification |
| plan               | Text      | Direct or Regular plan           |
| launch_date        | Date      | Scheme launch date               |
| benchmark          | Text      | Benchmark index                  |
| expense_ratio_pct  | Float     | Expense ratio percentage         |
| exit_load_pct      | Float     | Exit load percentage             |
| min_sip_amount     | Integer   | Minimum SIP amount               |
| min_lumpsum_amount | Integer   | Minimum lumpsum investment       |
| fund_manager       | Text      | Fund manager name                |
| risk_category      | Text      | Risk classification              |

 2. NAV History Dataset

| Column Name | Data Type | Description       |
| ----------- | --------- | ----------------- |
| amfi_code   | Integer   | Scheme identifier |
| date        | Date      | NAV date          |
| nav         | Float     | Net Asset Value   |

 3. Investor Transactions Dataset

| Column Name        | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | Text      | Unique investor identifier |
| transaction_date   | Date      | Transaction date           |
| amfi_code          | Integer   | Scheme identifier          |
| transaction_type   | Text      | SIP, Lumpsum or Redemption |
| amount_inr         | Integer   | Transaction amount in INR  |
| state              | Text      | Investor state             |
| city               | Text      | Investor city              |
| city_tier          | Text      | T30 or B30 classification  |
| age_group          | Text      | Investor age group         |
| gender             | Text      | Investor gender            |
| annual_income_lakh | Float     | Annual income in lakhs     |
| payment_mode       | Text      | Payment method             |
| kyc_status         | Text      | KYC verification status    |

 4. Scheme Performance Dataset

| Column Name       | Data Type | Description                  |
| ----------------- | --------- | ---------------------------- |
| amfi_code         | Integer   | Scheme identifier            |
| return_1yr_pct    | Float     | One year return percentage   |
| return_3yr_pct    | Float     | Three year return percentage |
| return_5yr_pct    | Float     | Five year return percentage  |
| expense_ratio_pct | Float     | Expense ratio percentage     |
| aum_crore         | Integer   | Assets under management      |
| risk_grade        | Text      | Scheme risk grade            |

 Source

All datasets were provided as part of the Bluestock Mutual Fund Analytics Capstone Project.

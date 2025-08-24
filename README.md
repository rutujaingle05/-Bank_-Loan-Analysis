# -Bank_-Loan-Analysis
### 1. Background and Overview
The financial services industry heavily relies on loan data analysis to track business performance, mitigate risk, and improve decision-making.
In this project, we analyze a dataset of 38,576 loan records (24 attributes) to evaluate lending activities, repayment patterns, borrower profiles, and key financial health indicators.
The objective is to build actionable KPIs and visualizations that allow stakeholders (banks, NBFCs, fintech companies) to:
•	Track loan applications and repayments in real time.
•	Monitor borrower risk through DTI (Debt-to-Income) and interest rates.
•	Identify trends by geography, loan purpose, employment history, and home ownership.
•	Separate good loans from bad loans to evaluate portfolio quality.
### 2.Key Performance Indicators (KPIs) Requirements:
Total Loan Applications: We need to calculate the total number of loan applications received during a specified period. Additionally, it is essential to monitor the Month-to-Date (MTD) Loan Applications.
Total Funded Amount: Understanding the total amount of funds disbursed as loans is crucial. We also want to keep an eye on the MTD Total Funded Amount metric.
Total Amount Received: Tracking the total amount received from borrowers is essential for assessing the bank's cash flow and loan repayment. We should analyse the Month-to-Date (MTD) Total Amount Receive.
Average Interest Rate: Calculating the average interest rate across all loans which will provide insights into our lending portfolio's overall cost.
Average Debt-to-Income Ratio (DTI): Evaluating the average DTI for our borrowers helps us gauge their financial health. We need to compute the average DTI for all loans.



### 3. Data Structure Overview:-
id                                int64
address_state                    object
application_type                 object
emp_length                       object
emp_title                        object
grade                            object
home_ownership                   object
issue_date               datetime64[ns]
last_credit_pull_date    datetime64[ns]
last_payment_date        datetime64[ns]
loan_status                      object
next_payment_date        datetime64
member_id                         int64
purpose                          object
sub_grade                        object
term                             object
verification_status              object
annual_income                   float64
dti                             float64
installment                     float64
int_rate                        float64
loan_amount                       int64
total_acc                         int64
total_payment                     int64

###  4.Executive Summary
 Key Metrics 
•	Total Loan Applications: 38,576
•	MTD Loan Applications (Dec 2021): 4,314
•	Total Funded Amount: $435.76M
•	MTD Funded Amount (Dec 2021): $53.98M
•	Total Amount Received: $435.76M
•	Average Interest Rate: 12.05%
•	Average DTI: 13.33
## Good vs Bad Loans
The dataset shows 100% as both Good and Bad loans, which suggests either a data issue or missing loan status filtering. In practice:
•	Good Loans = Fully Paid / Current
•	Bad Loans = Charged Off / Default

### Insight Deep Dive
##  Monthly Trends (by Issue Date)
•	Loan applications & funding peak in December 2021 (4,314 applications, $54M funded).
•	Indicates seasonal demand — possibly linked to holiday expenses & year-end financial needs.
## Regional Analysis (by State)
•	Certain states dominate loan issuance, suggesting regional disparities.
•	Helps banks target underpenetrated markets and control risk in high-exposure states.
## Loan Term Distribution (Donut Chart)
•	Majority loans concentrated in 36-month terms, fewer in 60-months.
•	Shorter terms reduce credit risk but limit customer affordability.
## Employment Length Analysis
•	Most applications from borrowers with 5–10 years employment.
•	Longer tenure borrowers show lower default risk.
##  Loan Purpose Breakdown
•	Debt consolidation emerges as the leading reason for borrowing.
•	Other purposes: home improvement, credit card payoff, medical expenses.
•	Helps banks design custom loan products.
##  Home Ownership Analysis (Treemap)
•	Borrowers with mortgage status form the largest share.
•	Homeowners (fully owned) are lower risk, while renters tend to borrow smaller amounts.
### Recommendations
1.	Fix Good vs Bad Loan Classification
   Define Good = Fully Paid/Current, Bad = Charged Off/Default.
   Recompute KPIs for accurate portfolio quality assessment.
2.	Risk Management
   Monitor high DTI borrowers (>20%) closely.
   Offer restructuring or limit funding exposure in risky segments.
3.	Product Strategy
   Design customized products for debt consolidation, as it’s the most popular loan purpose.
 	Promote short-term loans in riskier borrower groups.
4.	Regional Focus
    Expand in under-served states while controlling exposure in regions with high default probability.
5.	Seasonality Insights
   Allocate more credit in Q4 when demand spikes.
	Use predictive models to anticipate funding requirements.
________________________________________
✅ Why this project is important 
•	Shows you can define KPIs from business needs.
•	Demonstrates technical ability (data aggregation, visualization, KPI design).
•	Proves you can tell a story with data — not just calculate numbers.
•	Employers want analysts who can connect data → insight → recommendation → business value











   
   

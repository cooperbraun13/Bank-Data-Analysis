## Quantified Self Project

### Project Overview

This project analyzes my personal financial data in relation to my academic schedule to identify spending patterns and make predictions about my spending behavior. By examining bank transactions from September 2024 to April 2025 alongside my academic calendar, I hope to gain insights into how my spending habits are influenced by academic events such as, exams, finals week, and holiday breaks.

### Dataset

The dataset consists of two primary tables:

1. **Bank Transaction Data** (`bank_data.csv`): Contains personal banking transactions from September 2024 to April 2025, including:
* Transaction date
* Description
* Transaction type
* Amount
* Current balance
* Status

2. **Academic Calendar Data** (`academic_data.csv`): Contains information about academic events during the same period, including:
* Date
* Academic event (Regular Classes, Finals Week, Holidays, etc.)
* Period type (Class Period, Break, Exam Period, etc.)

3. **Merged Data** (`merged_data.csv): A comprehensive dataset that combines financial transactions with academic context, including:
* Date: Transaction date
* Description: Description of the transaction
* Type: Transaction type (e.g., Debit Card, Direct Payment, Check Deposit)
* Amount: Transaction amount (positive for credits, negative for debits)
* Current balance: Account balance after the transaction
* Status: Transaction status (e.g., Posted)
* Transaction_Type: Classification as Credit or Debit
* Absolute_Amount: Absolute value of the transaction amount
* Day_of_Week: Day of the week for the transaction (e.g., Monday, Tuesday)
* Month: Month of the transaction
* Category: Spending category (e.g., Dining, Retail, Groceries, Transportation)
* Spending_Bin: Size classification of spending (Small: <$10, Medium: $10-$50, Large: $50-$100, Very Large: >$100)
* academic_event_type: Type of academic event (e.g., Regular Classes, Finals Week, Holidays)
* class_activity: Specific activity (e.g., Lecture, Exam, Quiz, Break)
* day_of_week: Day of the week (alternative format)
* period_type: Type of academic period (e.g., Class Period, Assessment Period, Break, Weekend)

The dataset spans 7 months (September 1st, 2024 to April 1st, 2025) with daily transactions, providing over 150 instances for analysis.

### Requirements

* Python 3.12
* Conda distribution

## Setup and Execution

1. **Create and activate environment**:
```bash
conda create -n quantified-self python=3.12
conda activate quantified-self
```

2. **Install dependencies**:
```bash
conda install pandas matplotlib seaborn jupyter scikit-learn
```

3. **Run the analysis**:
```bash
jupyter notebook
```

Then open `analysis.ipynb` in the Jupyter interface to explore the financial data analysis.
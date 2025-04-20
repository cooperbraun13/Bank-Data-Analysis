## Quantified Self Project

### Project Overview

This project analyzes my personal financial data in relation to my academic schedule to identify spending patterns and make predictions about my spending behavior. By examining bank transactions from September 2024 to April 2025 alongside my academic calendar, I hope to gain insights into how my spending habits are influenced by academic events such as, exams, finals week, and holiday breaks

### Dataset

The dataset consists of two primary tables:

1. **Bank Transaction Data** (`data/raw/bank_data.csv`): Contains personal banking transactions from September 2024 to April 2025, including:
* Transaction date
* Description
* Transaction type
* Amount
* Current balance
* Status

2. **Academic Calendar Data** (`data/raw/academic_data.csv`): Contains information about academic events during the same period, including:
* Data
* Academic event (Regular Classes, Finals Week, Holidays, etc.)
* Period type (Class Period, Break, Exam Period, etc.)

The dataset spans 7 months (September 1st, 2024 to April 1st, 2025) with daily transactions, providing over ___ instances for analysis
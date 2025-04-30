import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def load_data(bank_path, academic_path):
    """ 
    Loads banking and academic data from the CSV files
    """
    bank_data = pd.read_csv(bank_path)
    academic_data = pd.read_csv(academic_path)
    return bank_data, academic_data

def clean_bank_data(df):
    """ 
    Cleans banking data and creates features
    """
    # Convert date to datetime
    df["Date"] = pd.to_datetime(df["Date"])
    
    # Convert amount to float
    df["Amount"] = df["Amount"].astype(float)
    
    # Create debit (negative) and credit (positive) flags based on amount
    df["Transaction_Type"] = df["Amount"].apply(
        lambda amount: "Debit" if amount < 0 else "Credit"
    )
    
    # Absolute amount column
    df["Absolute_Amount"] = df["Amount"].abs()
    
    # Extract day of the week and month
    df["Day_of_Week"] = df["Date"].dt.day_name()
    df["Month"] = df["Date"].dt.strftime("%B")
    
    # Create transaction categories
    df["Category"] = df["Description"].apply(categorize_transaction)
    
    # Create spending bins
    df["Spending_Bin"] = df["Absolute_Amount"].apply(create_spending_bins)
    
    return df
    
def clean_academic_data(df):
    """ 
    Cleans academic data and create features
    """
    # Convert date to datetime
    df["date"] = pd.to_datetime(df["date"])
    
    # Extract day of week
    df["day_of_week"] = df["date"].dt.day_name()
    
    # Create period type
    df["period_type"] = df.apply(
        lambda row: get_period_type(row["academic_event_type"], row["class_activity"]), axis=1
    )
    
    return df
    
def categorize_transaction(description):
    """ 
    Categorizes transactions based on description
    """
    description = description.lower()
    
    # Make sure safeway fuel doesn't end up in groceries category
    if "safeway fuel" in description:
        return "Transportation"
    
    # Dining out and food/snacks
    dining_keywords = ["daves", "starbucks", "jersey", "chick", "kfc", "taco", 
                       "panda", "cookie", "thomas hammer", "chipotle", "mango", 
                       "domino", "qdoba", "caruso", "mizuna", "ramen", "mcdonald", 
                       "coffee", "lebanon", "teriyaki", "brew", "thai", "bistro", 
                       "crumbl", "wing", "cstore"]
    
    # Grocery stores
    grocery_keywords = ["groceries", "market", "huckleberry", "costco", "safeway",
                        "trader joe", "wm superc", "fred"]
    
    # Retail and general shopping
    retail_keywords = ["target", "dicks", "amazon", "etsy", "petsmart", "petco",
                       "diamond beauty", "heart of gold", "riot"]
    
    # Transportation and gas
    transport_keywords = ["maverik", "fuel", "exxon", "conoc", "marathon petro",
                          "gas", "wsdot"]
    
    # Utilities and bills
    utilities_keywords = ["comcast", "cashnet", "city of spokane"]
    
    # Banking and financial
    banking_keywords = ["zelle", "interest earned", "robinhood",
                        "venmo", "mobile check deposit"]
    
    # Subscriptions
    subscription_keywords = ["subscr"]
    
    # Parking
    parking_keywords = ["parkrite", "diamond parking", "pmusa"]
    
    # Rent
    rent_keywords = ["cooper george"]
    
    # Check dining keywords
    for keyword in dining_keywords:
        if keyword in description:
            return "Dining"
    
    # Check transportation keywords
    for keyword in transport_keywords:
        if keyword in description:
            return "Transportation"
        
    # Check grocery keywords
    for keyword in grocery_keywords:
        if keyword in description:
            return "Groceries"
        
    # Check utilities keywords
    for keyword in utilities_keywords:
        if keyword in description:
            return "Utilities"
        
    # Check banking keywords
    for keyword in banking_keywords:
        if keyword in description:
            return "Banking & Investments"
        
    # Check subscription keywords
    for keyword in subscription_keywords:
        if keyword in description:
            return "Subscriptions"
        
    # Check parking keywords
    for keyword in parking_keywords:
        if keyword in description:
            return "Parking"
        
    # Check rent keywords
    for keyword in rent_keywords:
        if keyword in description:
            return "Rent"
        
    # If theres no match
    return "Other"
    
def create_spending_bins(amount):
    """ 
    Creates spending bins for classification
    """
    if amount < 10:
        return "Small (Less than $10)"
    elif amount < 50:
        return "Medium ($10-$50)"
    elif amount < 100:
        return "Large ($50-$100)"
    else:
        return "Very Large (More than $100)"
    
def get_period_type(event_type, class_activity):
    """ 
    Categorize academic period types
    """
    event_type = event_type.lower()
    class_activity = class_activity.lower()
    
    if "exam" in class_activity or "exam" in event_type or "finals week" in event_type:
        return "Assessment Period"
    elif "quiz" in class_activity:
        return "Assessment Period"
    elif "break" in event_type or "holiday" in event_type or "vacation" in event_type:
        return "Break"
    elif "weekend" in event_type:
        return "Weekend"
    elif "study day" in event_type:
        return "Assessment Period"
    elif "lecture" in class_activity:
        return "Class Period"
    else:
        return "Other"
    
def merge_datasets(bank_df, academic_df):
    """
    Merges banking and academic datasets 
    """
    merged_df = pd.merge(bank_df, academic_df, left_on="Date", right_on="date", how="left")
    
    # Clean columns
    if "date" in merged_df.columns:
        merged_df.drop(["date"], axis=1, inplace=True)
    
    return merged_df
    
def plot_spending_distribution(bank_df, amount_limit=2000):
    """ 
    Plots spending distribution
    """
    debit_data = bank_df[bank_df["Transaction_Type"] == "Debit"]
    
    plt.figure(figsize=(10, 6))
    plt.hist(debit_data["Absolute_Amount"], bins=50, edgecolor="black")
    plt.title("Distribution of Spending Amounts", fontsize=16)
    plt.xlabel("Amount ($)", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.xlim(0, amount_limit)
    plt.grid(axis="y", alpha=0.3)
    plt.show()
    
def plot_spending_by_category(bank_df):
    """ 
    Plots total spending by category
    """
    debit_data = bank_df[bank_df["Transaction_Type"] == "Debit"]
    spending_by_category = debit_data.groupby("Category")["Absolute_Amount"].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(12, 6))
    spending_by_category.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Total Spending by Category", fontsize=16)
    plt.xlabel("Category", fontsize=12)
    plt.ylabel("Total Spending ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()
    
def plot_spending_by_day(bank_df):
    """ 
    Plots average spending by day of the week
    """
    debit_data = bank_df[bank_df["Transaction_Type"] == "Debit"]
    spending_by_day = debit_data.groupby("Day_of_Week")["Absolute_Amount"].mean()
    
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    spending_by_day = spending_by_day.reindex(day_order)
    
    plt.figure(figsize=(12, 6))
    spending_by_day.plot(kind="bar", color="lightcoral", edgecolor="black")
    plt.title("Average Spending by Day of Week", fontsize=16)
    plt.xlabel("Day of Week", fontsize=12)
    plt.ylabel("Average Spending ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()
    
def plot_spending_by_period(merged_df):
    """ 
    Plots average spending by academic period
    """
    merged_debit = merged_df[merged_df["Transaction_Type"] == "Debit"]
    spending_by_period = merged_debit.groupby("period_type")["Absolute_Amount"].mean()
    
    plt.figure(figsize=(10, 6))
    spending_by_period.plot(kind="bar", color="lightgreen", edgecolor="black")
    plt.title("Average Spending by Academic Period", fontsize=16)
    plt.xlabel("Academic Period Type", fontsize=12)
    plt.ylabel("Average Spending ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()
    
def get_spending_statistics(bank_df):
    """ 
    Returns key statistics about my spending patterns
    """
    debit_data = bank_df[bank_df["Transaction_Type"] == "Debit"]
    stats = {
        "average": debit_data["Absolute_Amount"].mean(),
        "median": debit_data["Absolute_Amount"].median(),
        "max": debit_data["Absolute_Amount"].max(),
        "min": debit_data["Absolute_Amount"].min(),
        "total": debit_data["Absolute_Amount"].sum(),
        "count": debit_data.shape[0]
    }
    
    # Top categories
    top_categories = debit_data.groupby("Category")["Absolute_Amount"].sum().sort_values(ascending=False)
    stats["top_categories"] = top_categories
    
    # Daily spending averages
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    daily_avg = debit_data.groupby("Day_of_Week")["Absolute_Amount"].mean().reindex(day_order)
    stats["daily_avg"] = daily_avg
    
    return stats

def plot_monthly_spending(bank_df):
    """ 
    Plots spending trends over the 7 months
    """
    debit_data = bank_df[bank_df["Transaction_Type"] == "Debit"]
    monthly_spending = debit_data.groupby("Month")["Absolute_Amount"].sum()
    month_order = ["November", "December", "January", "February", "March", "April"]
    monthly_spending = monthly_spending.reindex(month_order)
    
    plt.figure(figsize=(12, 6))
    monthly_spending.plot(kind="bar", color="lightblue", edgecolor="black")
    plt.title("Total Monthly Spending", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Total Spending ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    return monthly_spending

def get_period_spending_statistics(merged_df):
    """ 
    Analyzes spending patterns across different academic periods
    """
    debit_data = merged_df[merged_df["Transaction_Type"] == "Debit"]
    
    # Period statistics
    period_stats = debit_data.groupby("period_type")["Absolute_Amount"].agg(["mean", "median", "count", "sum"])
    
    # Category breakdown by period
    period_category = debit_data.groupby(["period_type", "Category"])["Absolute_Amount"].sum().unstack(fill_value=0)
    
    return period_stats, period_category

def run_hypothesis_tests(merged_df):
    """ 
    Runs three statistical hypothesis tests on spending data
    """
    debit_data = merged_df[merged_df["Transaction Type"] == "Debit"]
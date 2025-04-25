import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

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
    df["period_type"] = df["academic_event_type"].apply(get_period_type)
    
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
    
def get_period_type(event_type):
    """ 
    Categorize academic period types
    """
    
    
def merge_datasets(bank_df, academic_df):
    """
    Merges banking and academic datasets 
    """
    
    
def plot_spending_distribution(bank_df, amount_limit=200):
    """ 
    Plots spending distribution
    """
    
    
def plot_spending_by_category(bank_df):
    """ 
    Plots total spending by category
    """
    
    
def plot_spending_by_day(bank_df):
    """ 
    Plots average spending by day of the week
    """
    
    
def plot_spending_by_period(merged_df):
    """ 
    Plots average spending by academic period
    """
    
    
def perform_hypothesis_test(merged_df):
    """ 
    Performs hypothesis test comparing exam and class period spending
    """
    
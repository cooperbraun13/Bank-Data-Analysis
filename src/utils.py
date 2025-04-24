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
    
    
def clean_academic_data(df):
    """ 
    Cleans academic data and create features
    """
    
    
def categorize_transaction(description):
    """ 
    Categorizes transactions based on description
    """
    
    
def create_spending_bins(amount):
    """ 
    Creates spending bins for classification
    """
    
    
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
    
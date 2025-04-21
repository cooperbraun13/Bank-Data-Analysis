import pandas as pd
import numpy as np
from datetime import datetime

def load_data(bank_file_path, academic_file_path):
    """ 
    Load raw bank and academic event data
    """
    bank_df = pd.read_csv("/data/raw/bank_data.csv")
    academic_df = pd.read_csv("/data/raw/academic_calendar.csv")
    
    return bank_df, academic_df

def clean_bank_data(bank_df):
    """ 
    Clean and preprocess bank transaction data
    """
    
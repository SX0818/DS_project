"""
Using method from paper: Predicting the milk yield curve of dairy cows in the subsequent lactation
Dataset: Merged_Sorted_Data_Herd_Daily PS: cloud has made changes to this file
"""

import pandas as pd

"""
data preprocessing
"""
# Load the Excel file
file_path = 'C:/Users/13593/Desktop/dsp/Data Analysis/your_file_path_here.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Display the first few rows of the data
print("First few rows of the data:")
print(data.head())

# Check for missing values
print("\nMissing values in the data:")
print(data.isnull().sum())

# Get basic statistics of the numerical columns
print("\nBasic statistics of the data:")
print(data.describe())

# Display the data types of each column
print("\nData types of each column:")
print(data.dtypes)

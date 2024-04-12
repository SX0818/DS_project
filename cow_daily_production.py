import pandas as pd
import csv
import os


# Load the data from CSV
file_path = 'Milking - Cow Daily Production.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# # Filter out summary rows based on 'Cow Number' column
# filtered_data = data[~data['Cow Number'].isin(['AVG', 'SUM'])]

# # Convert 'Cow Number' to integer (if not already)
# filtered_data['Cow Number'] = filtered_data['Cow Number'].astype(int)

# # Sort the data by 'Robot', 'Group number', and 'Cow Number'
# sorted_data = filtered_data.sort_values(by=['Robot', 'Group number', 'Cow Number'])

# # Display or save the sorted data
# print(sorted_data.head())  # Display the first few rows of the sorted data

# # Optionally, save the sorted data to a new CSV file
# sorted_data.to_csv('sorted_cow_data.csv', index=False)

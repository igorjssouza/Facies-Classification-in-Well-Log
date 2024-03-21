import pandas as pd
import os
from datetime import datetime

def import_csv_files(folder_path):
    # Get a list of all CSV files in the specified folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # Initialize an empty list to store DataFrames
    dataframes = []

    # Loop through each CSV file and append its data to the list
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        df = df[df != -9999].dropna()
        dataframes.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    combined_data = pd.concat(dataframes, ignore_index=True)

    return combined_data

# Specify the folder path where your CSV files are located
folder_path = 'well_north_sea_i2g'

# Call the function to import and combine the CSV files
result_df = import_csv_files(folder_path)

# Get the current timestamp for unique file naming
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

# Export the combined DataFrame to a new CSV file
output_csv_path = f'combined_data_{current_time}.csv'
result_df.to_csv(output_csv_path, index=False)
print(f"Combined data exported to {output_csv_path}")

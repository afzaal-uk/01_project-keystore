# Part 1 — The imports
#------------------------------------------------

import pandas as pd #main data handling libraray
import glob #find files matching name pattern
import os #handle file paths
import datetime

# Part 2 — Finding and loading all the files
#------------------------------------------------

folder = r"C:\01_project keystore\data\raw"
all_files = glob.glob(folder + r"\*.csv") #find all csv files in folder
print(f"Found {len(all_files)} files.Loading......\n")

tables = []
for i, file in enumerate(all_files):
    print(f"[{i+1}/{len(all_files)}] Loading {os.path.basename(file)}...", end=" ")
    df = pd.read_csv(file, encoding='latin-1', low_memory=False) #load csv file into pandas dataframe
    df['source_file'] = os.path.basename(file) #add a column with the source file name
    tables.append(df) #append dataframe to list
    print(f"done ({len(df):,} rows)")

combined = pd.concat(tables, ignore_index=True) #combine all dataframes into one
print(f"\nCombined table: {combined.shape[0]:,} rows, {combined.shape[1]:,} columns")

# Part 3 — Removing duplicate rows
#------------------------------------------------

before = combined.shape[0] #number of rows before removing duplicates
combined = combined.drop_duplicates() #remove duplicate rows
print(f"Removed {before - combined.shape[0]:,} duplicate rows. Remaining: {combined.shape[0]:,} rows")

# Part 4 — Fixing data types
#------------------------------------------------

combined["DATE"] = pd.to_datetime(combined["S_DATE"], errors='coerce') #convert date column to datetime
combined["PRICE"] = pd.to_numeric(combined["SELL"], errors='coerce') #convert price column to numeric

# Part 5 — Filtering out invalid rows
#------------------------------------------------

before = combined.shape[0] #number of rows before filtering
combined = combined[combined["PRICE"] >= 0] #filter out rows with negative price
combined = combined[combined["DATE"] <= datetime.datetime.now()] #filter out rows with future date
print(f"Removed {before - combined.shape[0]:,} invalid rows (negative price / future date)")

# Part 6 — Handling missing values
#------------------------------------------------

missing_before = combined.isnull().sum() #count missing values before handling
missing_before = missing_before[missing_before > 0] #filter to only columns with missing values
print("\nColumns with missing values before cleaning:")
print(missing_before)

for col in combined.columns:
    if pd.api.types.is_numeric_dtype(combined[col]):
        combined[col] = combined[col].fillna(combined[col].mean()) #fill missing numeric values with mean
    else:
        combined[col] = combined[col].fillna("unknown") #fill missing non-numeric values with "unknown"
print(f"\nTotal missing values after cleaning:", combined.isnull().sum().sum())

# Part 7 — Saving the final result
#------------------------------------------------
output_path = r"C:\01_project keystore\python\results\combined_cleaned_data.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True) #create output directory if it doesn't exist
combined.to_csv(output_path, index=False) #save combined dataframe to csv
print(f"\nSaved cleaned, combined dataset to: {output_path}")

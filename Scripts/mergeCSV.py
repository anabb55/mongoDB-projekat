import pandas as pd
import glob

# Specify the path to your CSV files
path = r"C:\Users\Hp\Desktop\dataSbp"

# Use glob to get all CSV files in the specified path
all_files = glob.glob(path + "/*.csv")

# Initialize an empty list to hold the dataframes
dfs = []

# Loop through the list of files and read each one into a dataframe
for filename in all_files:
    df = pd.read_csv(filename, low_memory=False)
    dfs.append(df)

# Concatenate all dataframes into one
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged dataframe to a new CSV file in the same directory
output_path = r"C:\Users\Hp\Desktop\dataSbp\merged_comments.csv"
merged_df.to_csv(output_path, index=False)

print(f"CSV files have been merged successfully and saved to {output_path}.")

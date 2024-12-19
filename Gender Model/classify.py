import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('input_file.csv')

# Check if '#CHROM' column contains 'Y'
has_Y = 'Y' in df['#CHROM'].values

# Print the result
if has_Y:
    print("The '#CHROM' column contains 'Y'.")
else:
    print("The '#CHROM' column does not contain 'Y'.")

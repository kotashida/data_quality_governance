import pandas as pd

def clean_and_profile(file_path):
    """Loads and cleans the Online Retail II dataset."""
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return

    # --- Initial Data Profile ---
    print("--- Initial Data Profile ---")
    print(f"Dataset shape: {df.shape}")
    print("\nColumn data types:")
    df.info()
    print("\nSummary statistics:")
    print(df.describe())
    print("\nMissing values:")
    print(df.isnull().sum())

    # --- Data Cleaning ---
    print("\n--- Data Cleaning ---")

    # Drop rows where CustomerID or Description is missing.
    df.dropna(subset=['Customer ID', 'Description'], inplace=True)
    print(f"Shape after dropping null CustomerID/Description: {df.shape}")

    # Remove canceled transactions (Invoice starts with 'C').
    df = df[~df['Invoice'].astype(str).str.startswith('C')]
    print(f"Shape after removing canceled transactions: {df.shape}")

    # Remove duplicate rows.
    df.drop_duplicates(inplace=True)
    print(f"Shape after dropping duplicates: {df.shape}")

    # Convert InvoiceDate to a proper datetime format.
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # --- Final Data Profile ---
    print("\n--- Final Data Profile ---")
    print(f"Final cleaned shape: {df.shape}")
    print("\nColumn data types after cleaning:")
    df.info()
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    return df

if __name__ == '__main__':
    DATA_FILE = 'data/online_retail_II.xlsx'
    CLEANED_DATA_FILE = 'data/online_retail_II_cleaned.csv'

    print(f'Cleaning and profiling {DATA_FILE}...')
    cleaned_df = clean_and_profile(DATA_FILE)
    if cleaned_df is not None:
        print('\nData cleaning and profiling complete.')
        # Save the cleaned data to a new CSV file.
        cleaned_df.to_csv(CLEANED_DATA_FILE, index=False)
        print(f'Cleaned data saved to {CLEANED_DATA_FILE}')

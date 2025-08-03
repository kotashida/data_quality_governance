from download_data import extract_data
from clean_and_profile import clean_and_profile
from generate_report import generate_report
import pandas as pd

# Define file paths
ZIP_PATH = 'data/online+retail+ii.zip'
DATA_DIR = 'data'
DATA_FILE = f'{DATA_DIR}/online_retail_II.xlsx'
CLEANED_DATA_FILE = f'{DATA_DIR}/online_retail_II_cleaned.csv'
REPORT_FILE = 'data_quality_report.html'

def main():
    """Runs the entire data quality workflow."""
    print("--- Starting Data Quality Project ---")

    # Step 1: Extract data from the zip archive.
    print("\nStep 1: Extracting data...")
    extract_data(ZIP_PATH, DATA_DIR)
    print("Data extracted successfully.")

    # Step 2: Clean and profile the dataset.
    print("\nStep 2: Cleaning and profiling data...")
    cleaned_df = clean_and_profile(DATA_FILE)
    if cleaned_df is not None:
        cleaned_df.to_csv(CLEANED_DATA_FILE, index=False)
        print(f"Cleaned data saved to {CLEANED_DATA_FILE}")

        # Step 3: Generate the final HTML report.
        print("\nStep 3: Generating data quality report...")
        generate_report(cleaned_df, REPORT_FILE)
        print(f"Report generated successfully at {REPORT_FILE}")
    else:
        print("Skipping report generation due to an error in the cleaning process.")

    print("\n--- Data Quality Project Finished ---")

if __name__ == '__main__':
    main()

import pandas as pd
from ydata_profiling import ProfileReport

def generate_report(df, output_file):
    """Generates a detailed HTML data quality report from a DataFrame."""
    # Create the report object.
    profile = ProfileReport(df, title="Data Quality Report", explorative=True)

    # Save the report to an HTML file.
    profile.to_file(output_file)

if __name__ == '__main__':
    CLEANED_DATA_FILE = 'data/online_retail_II_cleaned.csv'

    # Load the cleaned dataset.
    try:
        df = pd.read_csv(CLEANED_DATA_FILE)
    except FileNotFoundError:
        print(f"""Error: The file at {CLEANED_DATA_FILE} was not found.
Run clean_and_profile.py to generate it.""")

    # Generate and save the report.
    if 'df' in locals():
        REPORT_FILE = 'data_quality_report.html'
        print(f'Generating data quality report to {REPORT_FILE}...')
        generate_report(df, REPORT_FILE)
        print('Report generated successfully.')
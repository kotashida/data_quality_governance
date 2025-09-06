# Data Quality and Governance for Customer Transactions

## Project Goal

This project implements a robust data quality and governance workflow to profile, clean, and analyze a raw transactional dataset. The primary objective is to transform raw data into a reliable, high-quality dataset ready for analytical use while demonstrating key quantitative data validation techniques.

## Key Quantitative Skills Demonstrated

*   **Data Profiling & Descriptive Statistics:** Initial analysis of the dataset's statistical properties (mean, median, standard deviation) to identify anomalies and guide the cleaning strategy.
*   **Missing Value Analysis:** Systematic identification and removal of records with missing critical data points (e.g., `CustomerID`, `Description`) to ensure data integrity.
*   **Anomaly Detection:** Programmatic identification and filtering of invalid transactions, such as canceled orders, based on established business rules.
*   **Data Deduplication:** Application of algorithms to identify and remove duplicate records, ensuring each transaction is unique.
*   **Automated Reporting:** Generation of a comprehensive, interactive data quality report summarizing key metrics, variable distributions, correlations, and missing data patterns.

## Methodology

The project follows a structured, multi-step approach to ensure data quality:

1.  **Data Acquisition & Extraction**: The "Online Retail II" dataset from the UCI Machine Learning Repository is used. This real-world dataset contains transactional data, providing a realistic context for applying data governance principles. The initial script automates the extraction of this data from its compressed format.

2.  **Quantitative Data Profiling**: Before any cleaning, an initial data profile is established using `pandas`. This involves:
    *   **Descriptive Statistics:** Calculating metrics like mean, standard deviation, and quartiles for numerical columns (`Quantity`, `Price`) to understand their distribution and identify potential outliers.
    *   **Structural Analysis:** Examining the dataset's shape, column data types, and memory usage to get a baseline understanding.
    *   **Missing Value Quantification:** Calculating the exact number and percentage of null values for each variable. This is a critical step to justify the subsequent cleaning operations. For instance, `CustomerID` has a significant number of missing entries, which directly impacts the ability to perform customer-level analysis.

3.  **Data Cleaning & Validation**: A series of rule-based cleaning operations are performed. The choice of these rules is directly informed by the initial data profile:
    *   **Handling Missing Data:** Rows with missing `CustomerID` or `Description` are dropped. This is because `CustomerID` is essential for any user-based analysis, and a missing `Description` leaves the transaction with little informational value.
    *   **Filtering Invalid Transactions:** Canceled transactions, identified by invoices starting with 'C', are removed. This is a necessary step to ensure that analytical models are not skewed by transactions that were never completed.
    *   **Deduplication:** Duplicate rows are identified and removed to prevent the artificial inflation of transaction counts and revenue metrics.
    *   **Type Standardization:** The `InvoiceDate` column is converted to a proper datetime format, enabling time-series analysis.

4.  **Automated Reporting**: The `ydata-profiling` library is used to generate a detailed, interactive HTML report. This report serves as the final output of the governance process, providing a deep and quantifiable overview of the cleaned dataset's quality, including variable distributions, correlation matrices, and a final assessment of missing values.

## Quantified Results

The cleaning process had a measurable impact on the dataset's quality:

*   **Initial State:** The raw dataset contains **1,067,371** transactions.
*   **Missing Data Removal:** After removing rows with null `CustomerID` or `Description`, the dataset was reduced to **824,364** transactions.
*   **Canceled Transaction Removal:** Removing canceled orders further reduced the dataset to **805,620** transactions.
*   **Deduplication:** The final step of removing duplicate entries resulted in a cleaned dataset of **785,940** unique, valid transactions.
*   **Overall Reduction:** The entire cleaning process removed **281,431** records, representing a **26.4%** reduction in size, significantly improving the dataset's integrity.

## How to Run the Project

### Prerequisites

*   Python 3.x
*   pip (Python package installer)

### 1. Installation

Install the necessary Python libraries by running:

```bash
pip install -r requirements.txt
```

### 2. Execution

Execute the main script from the project's root directory:

```bash
python src/main.py
```

The script will output its progress to the console.

## Project Structure

```
.
├── data/
│   ├── online_retail_II.xlsx
│   ├── online_retail_II_cleaned.csv
│   └── online+retail+ii.zip
├── src/
│   ├── clean_and_profile.py
│   ├── download_data.py
│   ├── generate_report.py
│   └── main.py
├── data_quality_report.html
└── requirements.txt
```

## Output

1.  **Cleaned Data (`online_retail_II_cleaned.csv`):** A CSV file in the `data/` directory containing the cleaned, analysis-ready dataset.
2.  **Data Quality Report (`data_quality_report.html`):** An interactive HTML file in the root directory that provides a comprehensive profile of the final dataset.

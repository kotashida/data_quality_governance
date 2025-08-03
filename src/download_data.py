import zipfile
import os

def extract_data(zip_path, extract_to="."):
    """Extracts the dataset from a zip file into the target directory."""
    # Ensure the target directory exists.
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

if __name__ == '__main__':
    # Define paths
    ZIP_PATH = 'data/online+retail+ii.zip'
    DATA_DIR = 'data'

    print(f'Extracting data to {DATA_DIR}...')
    extract_data(ZIP_PATH, DATA_DIR)
    print('Data extracted successfully.')

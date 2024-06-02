import py7zr
import zipfile
import pandas as pd
from pathlib import Path

def extract_zip(file_path: str) -> Path:
    extraction_path = Path("C:/Users/14086/Downloads/sbr-app/instacart_data")
    extraction_path.mkdir(parents=True, exist_ok=True)
    
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extraction_path)
    
    # Extract nested zip files
    extracted_files = list(extraction_path.glob("*.zip"))
    for nested_zip in extracted_files:
        with zipfile.ZipFile(nested_zip, 'r') as zip_ref:
            zip_ref.extractall(extraction_path)
    
    return extraction_path  # Return the path where files are extracted

def read_csv_files(extraction_path: Path) -> list[tuple[str, pd.DataFrame]]:
    csv_files = list(extraction_path.glob("*.csv"))
    dataframes = []
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        dataframes.append((csv_file.stem, df))  # Use the stem (filename without suffix) as the table name
    if not dataframes:
        raise FileNotFoundError(f"No CSV files found in {extraction_path}")
    return dataframes

from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models, crud, utils
import os
import logging

app = FastAPI()

# Configure logging to print to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create the database tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "FastAPI server is running"}

@app.post("/upload/")
async def upload_file():
    try:
        # Update this path to your local zip file path
        file_path = r"C:/Users/14086/Downloads/sbr-app/instacart-market-basket-analysis.zip"
        logger.info(f"Processing file: {file_path}")
        
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            raise HTTPException(status_code=404, detail="File not found")

        # Extract the 7zip files from the uploaded zip file
        extraction_path = utils.extract_zip(file_path)
        logger.info(f"Extracted files in path: {extraction_path}")
        
        db: Session = SessionLocal()
        
        # Read the extracted CSV files into DataFrames
        try:
            dataframes = utils.read_csv_files(extraction_path)
            for table_name, df in dataframes:
                logger.info(f"Read data from file: {table_name}")
                logger.info(f"Dataframe head: {df.head()}")  # Log the first few rows

                # Create a table and insert data into it
                crud.create_table_and_insert_data(db, table_name, df)
                logger.info(f"Inserted data into table: {table_name}")
        except Exception as e:
            logger.error(f"Error processing files in {extraction_path}: {e}")
        
        db.close()
        return {"message": "Files uploaded and data inserted successfully"}
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

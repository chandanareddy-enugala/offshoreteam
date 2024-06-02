from sqlalchemy import Table, Column, String
from sqlalchemy.orm import Session
import pandas as pd
from app.database import Base

def create_table_and_insert_data(db: Session, table_name: str, df: pd.DataFrame):
    # Define the table schema
    columns = [Column(col, String) for col in df.columns]
    table = Table(table_name, Base.metadata, *columns)
    
    # Create the table in the database
    Base.metadata.create_all(db.bind)
    
    # Insert data into the table
    df.to_sql(table_name, con=db.bind, if_exists='replace', index=False)

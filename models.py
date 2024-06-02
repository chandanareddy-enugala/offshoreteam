from sqlalchemy import Column, Integer, String, MetaData, Table
from app.database import Base

# Dynamic table creation function
def create_dynamic_table(table_name, columns):
    metadata = MetaData()
    return Table(table_name, metadata, *(Column(col, String) for col in columns))

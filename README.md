## Instacart Data Insights System Documentation

### Overview
This documentation provides a comprehensive overview of the Instacart Data Insights System, which comprises a FastAPI backend for data handling and a Streamlit frontend for data visualization. The system processes Instacart data, uploads and inserts it into a PostgreSQL database, and provides insights through various endpoints.

### System Architecture

1. **Backend (FastAPI)**
   - **Database Connection**: Set up a connection to the PostgreSQL database using SQLAlchemy.
   - **Data Models**: Define dynamic table creation for storing data.
   - **CRUD Operations**: Implement functions for checking table existence, data presence, and inserting data.
   - **Utility Functions**: Provide utilities for extracting and reading CSV files from a zip archive.
   - **Upload Endpoint**: Handle file upload, data extraction, and insertion into the database.
   - **Insights Endpoints**: Provide various data insights through multiple endpoints.

2. **Frontend (Streamlit)**
   - **Data Fetching**: Fetch data from FastAPI endpoints.
   - **Data Visualization**: Display data insights using Streamlit’s interactive tables and charts.

### Detailed Components

#### 1. Database Connection (`database.py`)
- **Engine**: Creates a connection to the PostgreSQL database.
- **SessionLocal**: Provides a database session for transactions.
- **Base**: Declarative base for SQLAlchemy models.

#### 2. Data Models (`models.py`)
- **Dynamic Table Creation**: Uses SQLAlchemy to dynamically create tables based on the columns of the uploaded CSV files.

#### 3. CRUD Operations (`crud.py`)
- **Table Existence Check**: Uses SQLAlchemy’s inspector to check if a table exists in the database.
- **Table Data Check**: Determines if a table already has data to avoid duplicate inserts.
- **Data Insertion**: Creates tables and inserts data into the database using Pandas and SQLAlchemy.

#### 4. Utility Functions (`utils.py`)
- **Extract Zip**: Extracts CSV files from a zip archive.
- **Read CSV Files**: Reads the extracted CSV files into Pandas DataFrames.

#### 5. Upload Endpoint (`upload.py`)
- **File Upload Handling**: Accepts file upload requests, processes the uploaded zip file, and inserts the data into the database.
- **Data Integrity**: Ensures data is only inserted if it doesn’t already exist.

#### 6. Insights Endpoints (`insights.py`)
- **Popular Products**: Returns the top 10 most frequently ordered products.
- **Popular Aisles**: Returns the top 10 aisles with the highest order counts.
- **Orders by Hour of Day**: Provides a distribution of orders by hour of the day.
- **Orders by Day of Week**: Provides a distribution of orders by day of the week.
- **Reordered Products**: Returns the top 10 most reordered products.
- **User Behavior**: Analyzes user order patterns and frequency.
- **User Count**: Returns the total number of unique users in the dataset.

#### 7. Main Application (`main.py`)
- **Router Inclusion**: Includes the upload and insights routers for handling respective endpoints.
- **CORS Middleware**: Configures CORS to allow cross-origin requests from the frontend.

#### 8. Frontend (Streamlit)
- **Data Fetching**: Fetches data from the FastAPI endpoints using HTTP requests.
- **Data Visualization**: Displays data insights using Streamlit’s interactive tables and charts.

### System Workflow

1. **Data Upload and Insertion**:
   - The user uploads a zip file containing the dataset through the `/upload/` endpoint.
   - The system extracts the CSV files, reads them into Pandas DataFrames, and inserts them into the PostgreSQL database.
   - Data integrity checks ensure that data is only inserted if it doesn’t already exist in the tables.

2. **Data Insights Retrieval**:
   - The frontend (Streamlit) fetches data insights from various FastAPI endpoints.
   - Insights include popular products, popular aisles, order distributions by time, reordered products, and user behavior.
   - The frontend displays these insights using interactive tables and charts for easy visualization and analysis.

### Performance and Optimization

- **Database Indexing**: Ensure that database tables are indexed on frequently queried columns to speed up data retrieval.
- **Efficient Data Loading**: The upload endpoint ensures that data loading is optimized and avoids redundant inserts.
- **Caching**: Implement caching for frequently accessed data to reduce database load and improve response times.

### Best Practices

- **Modular Architecture**: The system is designed to be modular, with separate files for database connection, data models, CRUD operations, utility functions, and endpoints.
- **Data Integrity**: Checks are in place to ensure data is not duplicated during the upload and insertion process.
- **Scalability**: The system can handle large datasets efficiently and can be scaled horizontally by deploying multiple instances of the FastAPI server.

### Usage

1. **Start the FastAPI Server**:
   - Run the FastAPI server using Uvicorn.
   ```sh
   uvicorn app.main:app --reload
   ```

2. **Start the Streamlit App**:
   - Run the Streamlit app to visualize the data insights.
   ```sh
   streamlit run streamlit_app.py
   ```

### Conclusion

This documentation provides a detailed overview of the Instacart Data Insights System, covering its architecture, components, and workflow. The system is designed to be modular, efficient, and scalable, ensuring seamless data processing and insightful visualizations for end-users.

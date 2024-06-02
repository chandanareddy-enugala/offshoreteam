### Execution Flow and Detailed Explanation

#### 1. **Starting the FastAPI Server**
   - **Command**: `uvicorn app.main:app --reload`
   - **Under the Hood**: Uvicorn starts the FastAPI server, which initializes the app and includes the upload and insights routers. The server listens for incoming requests on the specified host and port (default: `0.0.0.0:8000`).

#### 2. **Uploading and Inserting Data**
   - **Endpoint**: `POST /upload/`
   - **Flow**:
     1. **File Upload**: The user uploads a zip file containing the dataset to the `/upload/` endpoint.
     2. **File Extraction**:
        - **Function**: `utils.extract_zip(file_path)`
        - **Action**: Extracts CSV files from the uploaded zip file to a specified directory.
     3. **Read CSV Files**:
        - **Function**: `utils.read_csv_files(extraction_path)`
        - **Action**: Reads the extracted CSV files into pandas DataFrames.
     4. **Database Insertion**:
        - **Check for Data**: 
          - **Function**: `crud.table_has_data(engine, table_name)`
          - **Action**: Checks if the table exists and contains data to avoid duplicate inserts.
        - **Create Table and Insert Data**:
          - **Function**: `crud.create_table_and_insert_data(db, table_name, df)`
          - **Action**: Dynamically creates the table based on the DataFrame columns and inserts the data.
     5. **Response**: Returns a success message if the files are processed and data is inserted successfully.

#### 3. **Fetching Data Insights**
   - **Popular Products**:
     - **Endpoint**: `GET /insights/popular-products`
     - **Flow**:
       1. **Fetch Data**: Queries the `order_products__prior` and `products` tables.
       2. **Process Data**: Computes the top 10 most frequently ordered products.
       3. **Return Data**: Returns a list of dictionaries representing the popular products.
   - **Popular Aisles**:
     - **Endpoint**: `GET /insights/popular-aisles`
     - **Flow**:
       1. **Fetch Data**: Queries the `order_products__prior`, `products`, and `aisles` tables.
       2. **Process Data**: Computes the top 10 aisles with the highest order counts.
       3. **Return Data**: Returns a list of dictionaries representing the popular aisles.
   - **Orders by Hour of the Day**:
     - **Endpoint**: `GET /insights/order-hour-of-day`
     - **Flow**:
       1. **Fetch Data**: Queries the `orders` table.
       2. **Process Data**: Computes the distribution of orders by hour of the day.
       3. **Return Data**: Returns a dictionary representing the distribution.
   - **Orders by Day of the Week**:
     - **Endpoint**: `GET /insights/order-day-of-week`
     - **Flow**:
       1. **Fetch Data**: Queries the `orders` table.
       2. **Process Data**: Computes the distribution of orders by day of the week.
       3. **Return Data**: Returns a dictionary representing the distribution.
   - **Reordered Products**:
     - **Endpoint**: `GET /insights/reordered-products`
     - **Flow**:
       1. **Fetch Data**: Queries the `order_products__prior` and `products` tables.
       2. **Process Data**: Computes the top 10 most reordered products.
       3. **Return Data**: Returns a list of dictionaries representing the reordered products.
   - **User Behavior**:
     - **Endpoint**: `GET /insights/user-behavior`
     - **Flow**:
       1. **Fetch Data**: Queries the `orders` table.
       2. **Process Data**: Analyzes user order patterns and frequency.
       3. **Return Data**: Returns a list of dictionaries representing user behavior metrics.

#### 4. **Visualizing Data in Streamlit**
   - **Command**: `streamlit run streamlit_app.py`
   - **Under the Hood**:
     - **Initialization**: Streamlit initializes the app and sets up the web server.
     - **Fetching Data**:
       - **Function**: `fetch_data(endpoint)`
       - **Action**: Sends HTTP GET requests to the specified FastAPI endpoints to fetch data.
     - **Displaying Data**:
       - **Components**:
         - **Tables**: Uses `st.table` to display data in tabular format.
         - **Charts**: Uses `st.bar_chart` to visualize data distributions.
     - **User Interaction**: Streamlit provides an interactive interface for users to view and interact with the data insights.

### Dynamic Table Creation

#### Explanation
- **Purpose**: Dynamically create database tables based on the structure of the uploaded CSV files, allowing flexibility to handle various datasets without predefined schemas.
- **Function**: `create_dynamic_table`
  - **Inputs**:
    - `table_name` (str): The name of the table to be created.
    - `columns` (list of str): A list of column names for the table.
  - **Process**:
    1. **Metadata Instance**: Creates a `MetaData` instance to hold information about tables and schemas.
    2. **Table Object**: Constructs a `Table` object with the specified name and columns. Each column is defined as a `String` type.
    3. **Return**: Returns the `Table` object for further use (e.g., creating the table in the database).
  - **Output**:
    - `Table`: A SQLAlchemy `Table` object representing the dynamically created table.

#### Example
- **Usage**: Called within `crud.create_table_and_insert_data` to create a table based on the DataFrame's columns before inserting data.
- **Flow**:
  1. **Extract Columns**: Extracts columns from the DataFrame.
  2. **Create Table**: Calls `create_dynamic_table` with the table name and extracted columns.
  3. **Insert Data**: Uses pandas `to_sql` method to insert data into the dynamically created table.

### Execution Flow Summary

1. **Start FastAPI server** with Uvicorn.
2. **Upload data** through `/upload/` endpoint.
   - Extract and read CSV files.
   - Check and insert data into dynamically created tables.
3. **Fetch data insights** through various `/insights/` endpoints.
   - Perform database queries and data processing.
   - Return processed data.
4. **Visualize data** with Streamlit.
   - Fetch data from FastAPI.
   - Display tables and charts interactively.

This detailed execution flow and explanation provide a clear understanding of how the system works and how each component interacts to provide the desired functionality.

# main.py
from database_connector import create_connection, create_table, upload_csv_to_db
from data_processing import read_data_from_db, clean_data, calculate_statistics
from data_visualization import visualize_data

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "covid_db"
}
table_name = "covid_data"
column_definitions = """
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    country VARCHAR(100),
    total_cases INT,
    total_deaths INT,
    total_recovered INT,
    new_cases INT,
    new_deaths INT,
    active_cases INT
"""

csv_file_path = "large_covid_data_sample.csv"

if __name__ == "__main__":
    # 1. Connect to the database
    mydb = create_connection(db_config)
    if not mydb:
        exit()

    # 2. Create the table (if it doesn't exist)
    create_table(mydb, table_name, column_definitions)

    # 3. Upload data from CSV to the database
    upload_csv_to_db(mydb, table_name, csv_file_path)
    mydb.close() # Close connection after upload

    # 4. Re-establish connection for reading and processing
    mydb_for_processing = create_connection(db_config)
    if not mydb_for_processing:
        exit()

    # 5. Read data from the database
    covid_df = read_data_from_db(db_config, table_name)
    mydb_for_processing.close() # Close connection after reading

    if covid_df is not None:
        # 6. Clean the data
        cleaned_df = clean_data(covid_df.copy())

        # 7. Perform statistical analysis
        calculate_statistics(cleaned_df)

        # 8. Visualize the data
        visualize_data(cleaned_df)
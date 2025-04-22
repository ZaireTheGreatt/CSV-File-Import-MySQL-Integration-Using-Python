# database_connector.py
import mysql.connector
import csv

def create_connection(db_config):
    """Creates and returns a MySQL connection."""
    try:
        mydb = mysql.connector.connect(**db_config)
        print("Successfully connected to the database!")
        return mydb
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def create_table(mydb, table_name, column_definitions):
    """Creates a table if it doesn't exist."""
    try:
        mycursor = mydb.cursor()
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {column_definitions}
        )
        """
        mycursor.execute(create_table_query)
        mydb.commit()
        print(f"Table '{table_name}' created or already exists.")
        mycursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

def upload_csv_to_db(mydb, table_name, csv_file_path):
    """Reads data from a CSV file and uploads it to the database."""
    try:
        mycursor = mydb.cursor()
        with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            placeholders = ', '.join(['%s'] * len(header))
            insert_query = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES ({placeholders})"
            
            for row in csv_reader:
                if len(row) == len(header):
                    mycursor.execute(insert_query, row)
                else:
                    print(f"Skipping row with mismatched columns: {row}")
        mydb.commit()
        print(f"Data from '{csv_file_path}' uploaded to '{table_name}'.")
        mycursor.close()
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
    except FileNotFoundError:
        print(f"Error: CSV file not found at '{csv_file_path}'")

if __name__ == "__main__":
    # Example usage if running directly
    db_config = {
        "host": "your_host",
        "user": "your_user",
        "password": "your_password",
        "database": "your_database"
    }
    table_name = "covid_data"
    
    # Updated column definitions to match your uploaded CSV
    column_definitions = """
        id INT AUTO_INCREMENT PRIMARY KEY,
        province VARCHAR(255),
        country VARCHAR(255),
        date DATE,
        total_cases INT,
        total_deaths INT,
        total_recovered INT,
        new_cases INT,
        new_deaths INT,
        active_cases INT
    """
    csv_file_path = "large_covid_data_sample.csv"

    mydb = create_connection(db_config)
    if mydb:
        create_table(mydb, table_name, column_definitions)
        upload_csv_to_db(mydb, table_name, csv_file_path)
        mydb.close()

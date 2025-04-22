# data_processing.py
import pandas as pd
import mysql.connector

def read_data_from_db(db_config, table_name):
    """Reads all data from the specified MySQL table into a Pandas DataFrame."""
    try:
        mydb = mysql.connector.connect(**db_config)
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, mydb)
        return df
    except mysql.connector.Error as err:
        print(f"Error reading data from database: {err}")
        return None
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
            print("Database connection closed after reading.")

def clean_data(df):
    """Performs basic data cleaning on the COVID-19 DataFrame."""
    print("Initial DataFrame info:")
    df.info()
    print("\nInitial DataFrame with null values:")
    print(df[df.isnull().any(axis=1)].head())

    # Handle missing values
    for col in ['total_cases', 'total_deaths', 'total_recovered',
                'new_cases', 'new_deaths', 'active_cases']:
        if col in df.columns:
            df[col].fillna(0, inplace=True)

    # Convert 'date' column to datetime if it exists
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    print("\nDataFrame info after cleaning:")
    df.info()
    print("\nDataFrame with null values after cleaning:")
    print(df[df.isnull().any(axis=1)].head())

    return df

def calculate_statistics(df):
    """Calculates various statistics from the DataFrame."""
    target_cols = ['total_cases', 'total_deaths', 'total_recovered']
    print("\nDescriptive Statistics:")
    print(df[target_cols].describe())

    print("\nCorrelation Matrix:")
    print(df[target_cols].corr())

    print("\nStandard Deviation:")
    print(df[target_cols].std())

    print("\nMeasures of Central Tendency:")
    for col in target_cols:
        if col in df.columns:
            print(f"\nStatistics for '{col}':")
            print(f"  Mean: {df[col].mean():.2f}")
            print(f"  Median: {df[col].median():.2f}")
            print(f"  Mode: {df[col].mode().tolist()}")
    return df

if __name__ == "__main__":
    # Example usage
    db_config = {
        "host": "your_host",
        "user": "your_user",
        "password": "your_password",
        "database": "your_database"
    }
    table_name = "covid_data"
    covid_df = read_data_from_db(db_config, table_name)
    if covid_df is not None:
        cleaned_df = clean_data(covid_df.copy())
        calculate_statistics(cleaned_df)

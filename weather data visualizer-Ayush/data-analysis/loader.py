import pandas as pd

def load_and_clean_data(filename):
    """
    Reads the CSV and fixes missing values.
    """
    print("--- Loading Data ---")
    try:
        # TASK 1: Load Data
        #df is dataframe
        df = pd.read_csv(filename)
        
        print("Data loaded successfully.")
        print("Initial Info:")
        print(df.info())

        # TASK 2: Cleaning
        # Convert date column to datetime objects
        df['Date'] = pd.to_datetime(df['Date'])

        # Fill missing values
        # Rule: Fill temp with mean, rain with 0
        mean_temp = df['Temperature_C'].mean()
        df['Temperature_C'] = df['Temperature_C'].fillna(mean_temp)
        df['Rainfall_mm'] = df['Rainfall_mm'].fillna(0)

        # Check if clean
        missing_count = df.isnull().sum().sum()
        print(f"\nCleaning done. Total missing values now: {missing_count}")
        
        return df

    except FileNotFoundError:
        print("Error: The file 'weather_data.csv' was not found.")
        return None
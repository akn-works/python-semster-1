import sys
# This ensures we can import from our local folders
sys.path.append('.')

from data_analysis import loader, stats
from visualization import plots

def main():
    print("=== Weather Analyzer Visualizer ===")
    
    # Step 1: Load and Clean
    #df- dataframe, it is like Excel Spreadsheet inside Python.
    # We pass the filename here
    df = loader.load_and_clean_data('weather_data.csv')
    
    if df is not None:
        # Step 2: Show Stats (NumPy)
        stats.show_numpy_stats(df)
        
        # Step 3: Grouping (Pandas)
        stats.show_monthly_averages(df)
        
        # Step 4: Visualizations (Matplotlib)
        plots.generate_plots(df)
        
        # Step 5: Export (Task 6)
        output_file = 'my_cleaned_data.csv'
        df.to_csv(output_file, index=False)
        print(f"\nSuccess! Cleaned data saved to '{output_file}'.")
        print("All tasks completed.")

if __name__ == "__main__":
    main()
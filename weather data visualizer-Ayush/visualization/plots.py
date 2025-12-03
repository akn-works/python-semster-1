import matplotlib.pyplot as plt
import pandas as pd

def generate_plots(df):
    """
    Creates and saves all the required plots.
    """
    print("\n--- Making Plots ---")

    # Plot 1: Daily Temp (Line Plot)
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Temperature_C'], color='orange', marker='o')
    plt.title('Daily Temperature Trend')
    plt.xlabel('Date')
    plt.ylabel('Temp (C)')
    plt.grid(True)
    plt.savefig('1_temp_trend.png')
    print("Saved: 1_temp_trend.png")
    # plt.show() # Uncomment if you want to see popups

    # Plot 2: Monthly Rain (Bar Chart)
    # We need to sum rainfall for this specific plot
    rain_sum = df.groupby('Month', observed=True)['Rainfall_mm'].sum()

    plt.figure(figsize=(10, 5))
    rain_sum.plot(kind='bar', color='blue')
    plt.title('Total Rainfall per Month')
    plt.ylabel('Rainfall (mm)')
    plt.tight_layout()
    plt.savefig('2_rain_bar.png')
    print("Saved: 2_rain_bar.png")

    # Plot 3: Scatter Plot (Temp vs Humidity)
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Temperature_C'], df['Humidity_Pct'], c='green')
    plt.title('Temperature vs Humidity')
    plt.xlabel('Temperature (C)')
    plt.ylabel('Humidity (%)')
    plt.savefig('3_scatter.png')
    print("Saved: 3_scatter.png")

    # Plot 4: Combined Subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Top graph (Temp)
    ax1.plot(df['Date'], df['Temperature_C'], 'r-')
    ax1.set_title('Temperature Trend')
    ax1.set_ylabel('Temp (C)')

    # Bottom graph (Humidity)
    ax2.plot(df['Date'], df['Humidity_Pct'], 'b-')
    ax2.set_title('Humidity Trend')
    ax2.set_ylabel('Humidity (%)')

    plt.tight_layout()
    plt.savefig('4_combined.png')
    print("Saved: 4_combined.png")
# data_visualization.py
import matplotlib.pyplot as plt
import pandas as pd

def visualize_data(df):
    """Creates visualizations of the COVID-19 data."""

    # Time series of total cases and deaths
    if 'date' in df.columns and 'total_cases' in df.columns and 'total_deaths' in df.columns:
        df_by_date = df.groupby('date')[['total_cases', 'total_deaths']].sum().reset_index()
        
        plt.figure(figsize=(12, 6))
        plt.plot(df_by_date['date'], df_by_date['total_cases'], label='Total Cases', marker='o')
        plt.plot(df_by_date['date'], df_by_date['total_deaths'], label='Total Deaths', marker='x')
        plt.xlabel('Date')
        plt.ylabel('Number of Cases')
        plt.title('COVID-19 Trends Over Time')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Top 10 countries by total cases
    if 'country' in df.columns and 'total_cases' in df.columns:
        top_countries = df.groupby('country')['total_cases'].max().nlargest(10)
        plt.figure(figsize=(10, 6))
        top_countries.plot(kind='bar', color='skyblue')
        plt.xlabel('Country')
        plt.ylabel('Total Confirmed Cases')
        plt.title('Top 10 Countries with Highest Confirmed COVID-19 Cases')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    # Active cases heatmap (optional)
    if 'country' in df.columns and 'active_cases' in df.columns:
        plt.figure(figsize=(10, 6))
        active = df.groupby('country')['active_cases'].max().nlargest(10)
        active.plot(kind='bar', color='orange')
        plt.xlabel('Country')
        plt.ylabel('Active Cases')
        plt.title('Top 10 Countries by Active COVID-19 Cases')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example test case
    data = {
        'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02']),
        'country': ['USA', 'USA', 'Canada', 'Canada'],
        'total_cases': [100, 150, 50, 75],
        'total_deaths': [5, 8, 2, 3],
        'active_cases': [95, 142, 48, 72]
    }
    temp_df = pd.DataFrame(data)
    visualize_data(temp_df)

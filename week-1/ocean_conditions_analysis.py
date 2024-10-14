import pandas as pd
import matplotlib.pyplot as plt

def load_ocean_conditions_data(file_path):
    """Load the ocean conditions dataset from the specified CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("Ocean conditions data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return None

def analyze_data(df):
    """Analyze the ocean conditions dataset to provide insights."""
    if df is None:
        return
    
    # Display basic information about the dataset
    print("\n--- Dataset Information ---")
    print(df.info())
    
    print("\n--- Summary Statistics ---")
    print(df.describe())

    # Visualize temperature distribution
    plt.figure(figsize=(10, 5))
    plt.hist(df['Temperature_C'], bins=10, color='lightgreen', alpha=0.7)
    plt.title('Temperature Distribution in Ocean Conditions')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.show()

    # Analyze and visualize correlations
    correlation_matrix = df.corr()
    print("\n--- Correlation Matrix ---")
    print(correlation_matrix)

    # Visualize correlation heatmap
    plt.figure(figsize=(8, 6))
    plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
    plt.title('Correlation Heatmap')
    plt.colorbar()
    plt.xticks(range(len(correlation_matrix)), correlation_matrix.columns, rotation=45)
    plt.yticks(range(len(correlation_matrix)), correlation_matrix.columns)
    plt.tight_layout()
    plt.show()

    # Additional Analysis: Average temperature by weather condition
    avg_temp_by_weather = df.groupby('Weather_Condition')['Temperature_C'].mean().reset_index()
    print("\n--- Average Temperature by Weather Condition ---")
    print(avg_temp_by_weather)

    # Create a bar plot for average temperature by weather condition
    plt.figure(figsize=(10, 5))
    plt.bar(avg_temp_by_weather['Weather_Condition'], avg_temp_by_weather['Temperature_C'], color='skyblue')
    plt.title('Average Temperature by Weather Condition')
    plt.xlabel('Weather Condition')
    plt.ylabel('Average Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Load the ocean conditions data from the CSV file
    FILE_PATH = 'Data/ocean_conditions_data.csv'
    ocean_conditions_data = load_ocean_conditions_data(FILE_PATH)
    analyze_data(ocean_conditions_data)

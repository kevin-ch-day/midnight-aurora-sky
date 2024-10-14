import pandas as pd
import random

def create_ocean_conditions_dataset():
    """
    Create a dataset of ocean conditions and save it as 'ocean_conditions_data.csv'.
    The dataset includes 100 samples with 7 features.

    Explanation of the Dataset:
    Sample_ID: Unique identifiers for each sample (S1, S2, ..., S100).
    Temperature_C: Random ocean temperature between 5°C and 30°C.
    Salinity_PPT: Random salinity in parts per thousand (PPT), simulating various oceanic conditions.
    Wave_Height_M: Random wave height ranging from 0.1 meters to 5.0 meters.
    Current_Speed_KPH: Random current speed between 0.5 KPH and 10 KPH.
    Depth_M: Random depth of the ocean measured in meters, between 1 and 100 meters.
    Weather_Condition: Randomly assigned weather conditions, including options like Sunny, Cloudy, Rainy, Stormy, and Foggy.
    """
    
    # Define the number of rows in the dataset
    num_rows = 150
    
    # Generate ocean condition data
    ocean_data = {
        "Sample_ID": [f"S{i + 1}" for i in range(num_rows)],
        "Temperature_C": [round(random.uniform(5.0, 30.0), 2) for _ in range(num_rows)],  # Random temperature between 5°C and 30°C
        "Salinity_PPT": [round(random.uniform(30.0, 40.0), 2) for _ in range(num_rows)],  # Random salinity in PPT
        "Wave_Height_M": [round(random.uniform(0.1, 5.0), 2) for _ in range(num_rows)],  # Random wave height between 0.1m and 5.0m
        "Current_Speed_KPH": [round(random.uniform(0.5, 10.0), 2) for _ in range(num_rows)],  # Random current speed between 0.5 and 10 KPH
        "Depth_M": [random.randint(1, 100) for _ in range(num_rows)],  # Random depth between 1m and 100m
        "Weather_Condition": random.choices(
            ["Sunny", "Cloudy", "Rainy", "Stormy", "Foggy"], k=num_rows
        ),  # Randomly assigned weather conditions
    }

    # Create a DataFrame from the generated data
    df = pd.DataFrame(ocean_data)

    # Define the CSV file name
    csv_file_name = "ocean_conditions_data.csv"

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_name, index=False)

    # Output a confirmation message
    print(f"Custom dataset created successfully and saved as '{csv_file_name}'.")
    print("Dataset includes the following columns:")
    print(", ".join(df.columns))

# Execute the dataset creation function
if __name__ == "__main__":
    create_ocean_conditions_dataset()

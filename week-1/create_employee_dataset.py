import pandas as pd
import random

# Title: Employee Dataset Generator
# Purpose: Create a custom employee dataset for data science exploration and save it as a CSV.

def create_custom_dataset():
    """
    Generate a custom dataset of employee information for analysis and save to CSV.
    The dataset includes 40 rows and 9 relevant columns.
    """
    
    # Define the number of rows in the dataset
    num_rows = 40
    
    # Generate employee data
    employee_data = {
        "Employee_ID": [f"E{1000 + i}" for i in range(num_rows)],
        "Name": [f"Employee_{i}" for i in range(num_rows)],
        "Age": [random.randint(22, 60) for _ in range(num_rows)],  # Random age between 22 and 60
        "Department": random.choices(
            ["HR", "Engineering", "Sales", "Marketing", "Finance"], k=num_rows
        ),  # Randomly assigned department
        "Salary": [random.randint(40000, 120000) for _ in range(num_rows)],  # Salary range
        "Joining_Year": [random.randint(2010, 2023) for _ in range(num_rows)],  # Random joining year
        "Performance_Score": [round(random.uniform(1.0, 5.0), 2) for _ in range(num_rows)],  # Performance rating
        "Years_in_Company": [random.randint(1, 12) for _ in range(num_rows)],  # Years at the company
        "Remote_Work": random.choices([True, False], k=num_rows)  # Boolean for remote work status
    }

    # Create a DataFrame from the generated data
    df = pd.DataFrame(employee_data)

    # Define the CSV file name
    csv_file_name = "employee_data.csv"

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_name, index=False)

    # Output a confirmation message
    print(f"Custom dataset created successfully and saved as '{csv_file_name}'.")
    print("Dataset includes the following columns:")
    print(", ".join(df.columns))

# Execute the dataset creation function
if __name__ == "__main__":
    create_custom_dataset()

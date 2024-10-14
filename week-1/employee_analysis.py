import pandas as pd
import matplotlib.pyplot as plt

def load_employee_data(file_path):
    """Load the dataset from the specified CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
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
    """Analyze the employee dataset to provide insights."""
    if df is None:
        return
    
    # Display basic information about the dataset
    print("\n--- Dataset Information ---")
    print(df.info())
    
    print("\n--- Summary Statistics ---")
    print(df.describe(include='all'))  # Include all columns in summary statistics

    # Check for missing values
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    # Group by department and calculate average salary
    avg_salary = df.groupby('Department')['Salary'].mean().reset_index()
    print("\n--- Average Salary by Department ---")
    print(avg_salary)

    # Create a bar plot for average salary by department
    plt.figure(figsize=(10, 5))
    plt.bar(avg_salary['Department'], avg_salary['Salary'], color='skyblue')
    plt.title('Average Salary by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Salary')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Additional Analysis: Salary Distribution
    plt.figure(figsize=(10, 5))
    plt.hist(df['Salary'], bins=20, color='lightgreen', alpha=0.7)
    plt.title('Salary Distribution of Employees')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.show()

    # Analyze the relationship between Age and Salary
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Age'], df['Salary'], color='purple', alpha=0.6)
    plt.title('Salary vs Age of Employees')
    plt.xlabel('Age')
    plt.ylabel('Salary')
    plt.grid()
    plt.tight_layout()
    plt.show()

    # Analyze employee count by department
    employee_count = df['Department'].value_counts()
    plt.figure(figsize=(10, 5))
    plt.bar(employee_count.index, employee_count.values, color='orange', alpha=0.7)
    plt.title('Number of Employees by Department')
    plt.xlabel('Department')
    plt.ylabel('Number of Employees')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Load the employee data from the CSV file
    FILE_PATH = 'Data/employee_data.csv'
    employee_data = load_employee_data(FILE_PATH)
    analyze_data(employee_data)

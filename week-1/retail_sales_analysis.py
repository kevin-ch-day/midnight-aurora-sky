import pandas as pd
import matplotlib.pyplot as plt

def load_retail_sales_data(file_path):
    """Load the retail sales dataset from the specified CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("Retail sales data loaded successfully.")
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
    """Analyze the retail sales dataset to provide insights."""
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

    # Calculate total sales and add a new column
    df['Total_Sales'] = df['Quantity_Sold'] * df['Sale_Price']
    total_sales = df['Total_Sales'].sum()
    print(f"\nTotal Sales: ${total_sales:.2f}")

    # Visualize total sales by product category
    category_sales = df.groupby('Product_Category')['Total_Sales'].sum().reset_index()
    
    plt.figure(figsize=(10, 5))
    plt.bar(category_sales['Product_Category'], category_sales['Total_Sales'], color='coral')
    plt.title('Total Sales by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Additional Analysis: Sales Trends Over Time
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])  # Convert to datetime
    sales_trend = df.groupby(df['Order_Date'].dt.to_period("M"))['Total_Sales'].sum().reset_index()

    plt.figure(figsize=(10, 5))
    plt.plot(sales_trend['Order_Date'].dt.to_timestamp(), sales_trend['Total_Sales'], marker='o', color='blue')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales ($)')
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Load the retail sales data from the CSV file
    FILE_PATH = 'Data/retail_sales_data.csv'
    retail_sales_data = load_retail_sales_data(FILE_PATH)
    analyze_data(retail_sales_data)

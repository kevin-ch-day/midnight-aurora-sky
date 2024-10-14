import pandas as pd
import random
from datetime import datetime, timedelta

def create_retail_sales_dataset():
    """
    Create a dataset of retail sales and save it as 'retail_sales_data.csv'.
    The dataset includes 100 samples with 12 features.
    
    Explanation of the Dataset:
    Order_ID: Unique identifiers for each order (O1, O2, ..., O100).
    Product_Name: Randomly assigned product names.
    Quantity_Sold: Number of items sold in the transaction.
    Sale_Price: Sale price per item in USD.
    Total_Sales: Total sales amount for the transaction.
    Order_Date: Date of the transaction.
    Customer_Age: Age of the customer making the purchase.
    Customer_Gender: Gender of the customer (Male/Female/Other).
    Payment_Method: Payment method used for the transaction.
    Shipping_Cost: Cost of shipping for the order.
    Order_Status: Current status of the order (Shipped/Processing/Cancelled).
    Product_Category: Category of the product sold.
    """
    
    # Define the number of rows in the dataset
    num_rows = 100
    
    # Generate retail sales data
    product_names = [f"Product_{i+1}" for i in range(20)]  # 20 different products
    order_data = {
        "Order_ID": [f"O{i + 1}" for i in range(num_rows)],
        "Product_Name": random.choices(product_names, k=num_rows),  # Randomly assigned product names
        "Quantity_Sold": [random.randint(1, 10) for _ in range(num_rows)],  # Random quantity sold
        "Sale_Price": [round(random.uniform(10.0, 100.0), 2) for _ in range(num_rows)],  # Sale price per item
        "Total_Sales": [],  # Will calculate later
        "Order_Date": [(datetime.now() - timedelta(days=random.randint(0, 30))).date() for _ in range(num_rows)],  # Random order date within the last 30 days
        "Customer_Age": [random.randint(18, 65) for _ in range(num_rows)],  # Random customer age
        "Customer_Gender": random.choices(["Male", "Female", "Other"], k=num_rows),  # Randomly assigned customer gender
        "Payment_Method": random.choices(["Credit Card", "PayPal", "Bank Transfer"], k=num_rows),  # Random payment methods
        "Shipping_Cost": [round(random.uniform(5.0, 25.0), 2) for _ in range(num_rows)],  # Random shipping cost
        "Order_Status": random.choices(["Shipped", "Processing", "Cancelled"], k=num_rows),  # Random order statuses
        "Product_Category": random.choices(["Electronics", "Clothing", "Home & Garden", "Toys", "Sports"], k=num_rows)  # Random product categories
    }

    # Calculate Total Sales
    order_data["Total_Sales"] = [
        round(order_data["Quantity_Sold"][i] * order_data["Sale_Price"][i], 2)
        for i in range(num_rows)
    ]

    # Create a DataFrame from the generated data
    df = pd.DataFrame(order_data)

    # Define the CSV file name
    csv_file_name = "retail_sales_data.csv"

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_name, index=False)

    # Output a confirmation message
    print(f"Custom dataset created successfully and saved as '{csv_file_name}'.")
    print("Dataset includes the following columns:")
    print(", ".join(df.columns))

# Execute the dataset creation function
if __name__ == "__main__":
    create_retail_sales_dataset()

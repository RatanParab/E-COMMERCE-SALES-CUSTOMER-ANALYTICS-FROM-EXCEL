import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import create_engine


df = pd.read_csv("ecommerce_sales_customer_analytics_cleaned.csv")



# 1.How much total revenue did the business generate?


total_revenue = df['Revenue'].sum()

# print("Total Revenue:", total_revenue)


# 2.Average Revenue per Order

average_order_value = df['Revenue'].mean()

# print("Average Order Value:", average_order_value)


# 3.Total Orders

total_orders = len(df)

# print("Total Orders:", total_orders)


# for checking order id is unique
# print("Unique Orders:", df['Order_ID'].nunique())
# print("Total Rows:", len(df))


# 4.Revenue by Category

category_revenue = df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)

# print(category_revenue)


# 5.Revenue by City

city_revenue = df.groupby('City')['Revenue'].sum().sort_values(ascending=False)

# print(city_revenue)


# 6.Revenue by Customer Type

customer_type_revenue = df.groupby('Customer_Type')['Revenue'].sum().sort_values(ascending=False)

# print(customer_type_revenue)


# 7.Order Status Analysis
order_status_count = df['Order_Status'].value_counts()

# print(order_status_count)


# 8.Payment Mode Analysis
payment_count = df['Payment_Mode'].value_counts()

# print(payment_count)


# 9.Monthly Revenue Trend

df['Order_Date'] = pd.to_datetime(df['Order_Date'])


monthly_revenue = df.groupby(
    df['Order_Date'].dt.to_period('M')
)['Revenue'].sum()

# print(monthly_revenue)



# 10.Customer Age Distribution

# print(df['Age'].describe())





username = "postgres"
password = "Ratan@123"
host = "localhost"
port = 5433
database = "ecommerce_analysis"

connection_url = URL.create(
    "postgresql+psycopg2",
    username=username,
    password=password,
    host=host,
    port=port,
    database=database
)

engine = create_engine(connection_url)

table_name = "ecommerce"

df.to_sql(
    table_name,
    engine,
    if_exists="replace",
    index=False
)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")
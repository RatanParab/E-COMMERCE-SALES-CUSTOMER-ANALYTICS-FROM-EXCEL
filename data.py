import pandas as pd

df = pd.read_csv("ecommerce_sales_customer_analytics_raw.csv")

# print(df.head())

# print(df.shape)
# print(df.columns)
# print(df.info())


# where the duplicate and null is 

# print(df.isnull().sum())
# print(df.isnull().sum().sum())
# print("Duplicate rows:", df.duplicated().sum())



          #  handling null
          
# how many and in which way

# print(df['Age'].describe())
# print(df['City'].value_counts())
# print(df['Payment_Mode'].value_counts())
# print(df['Rating'].describe())



# handle it 

df.loc[df['Age'] > 100, 'Age'] = pd.NA  # bcz we find that there is unrealistic age of 120

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Rating'] = df['Rating'].fillna(df['Rating'].median())
df['Payment_Mode'] = df['Payment_Mode'].fillna('Unknown')
df['City'] = df['City'].fillna('Unknown')


# ensure 
# print(df.isnull().sum())



                 # handling duplicates
                 
# find 

duplicates = df[df.duplicated()]

# print(duplicates)
# print(duplicates.shape)



# handle
df = df.drop_duplicates()

# print("Shape after removing duplicates:", df.shape)
# print("Duplicate rows:", df.duplicated().sum())




# print("Age values:")
# print(df['Age'].describe())

# print("\nQuantity values:")
# print(df['Quantity'].value_counts().sort_index())

# print("\nUnit Price values:")
# print(df['Unit_Price'].describe())

# print("\nDiscount values:")
# print(df['Discount'].describe())

# print("\nShipping Days values:")
# print(df['Shipping_Days'].value_counts().sort_index())

# print("\nRating values:")
# print(df['Rating'].describe())


# problemetic part
# print("Invalid Quantity rows:")
# print(df[df['Quantity'] <= 0])

# print("\nInvalid Unit Price rows:")
# print(df[df['Unit_Price'] <= 0])


# Remove invalid quantity and unit price records
df = df[(df['Quantity'] > 0) & (df['Unit_Price'] > 0)]

# print("Shape after removing invalid records:", df.shape)



#final check

# print("Invalid Quantity:", (df['Quantity'] <= 0).sum())
# print("Invalid Unit Price:", (df['Unit_Price'] <= 0).sum())

# print("Final shape:", df.shape)



            #date-time


# Convert Order_Date to datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# print(df['Order_Date'].dtype)

             
             #category

# print(df['Category'].unique())

df['Category'] = df['Category'].str.strip().str.title()

# print(df['Category'].unique())




# one check to others also 

# print(df['Category'].value_counts())
# print("\nTotal categories:", df['Category'].nunique())

# print("City:")
# print(df['City'].unique())

# print("\nPayment Mode:")
# print(df['Payment_Mode'].unique())

# print("\nCustomer Type:")
# print(df['Customer_Type'].unique())

# print("\nOrder Status:")
# print(df['Order_Status'].unique())






# creating columns for analysis 

df['Revenue'] = df['Quantity'] * df['Unit_Price'] * (1 - df['Discount'])


# to verify
# print(df[['Quantity', 'Unit_Price', 'Discount', 'Revenue']].head())
# print(df['Revenue'].describe())



# convert to cleaned csv

df.to_csv("ecommerce_sales_customer_analytics_cleaned.csv", index=False)

print("Cleaned dataset saved successfully.")

print(df.shape)
print(df.head())
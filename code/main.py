import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file into a pandas DataFrame
df = pd.read_csv('')

# Drop duplicates
df.drop_duplicates(inplace=True)

# Fill missing values with 0
df['no_of_ratings'].fillna(0, inplace=True)

# Convert data types
df['discount_price'] = df['discount_price'].astype(float)
df['actual_price'] = df['actual_price'].astype(float)

# Compute basic statistics
mean_ratings = df['ratings'].mean()
median_discount = df['discount_price'].median()
std_actual = df['actual_price'].std()

# Visualize data with a histogram
plt.hist(df['ratings'], bins=10)
plt.xlabel('Ratings')
plt.ylabel('Count')
plt.show()

# Compute average discount percentage
df['discount_percentage'] = (df['actual_price'] - df['discount_price']) / df['actual_price']
mean_discount_pct = df['discount_percentage'].mean()

# Compute sales by main category
sales_by_main = df.groupby('main_category')['discount_price'].sum()

# Compute average number of ratings by sub-category
ratings_by_sub = df.groupby('sub_category')['no_of_ratings'].mean()


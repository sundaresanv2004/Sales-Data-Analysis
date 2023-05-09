import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Updated_Shoes.csv')

# Check for missing values
print(data.isnull().sum())

# Drop duplicates
data.drop_duplicates(inplace=True)

# Convert data types if necessary
data['discount_price'] = data['discount_price'].astype(float)
data['actual_price'] = data['actual_price'].astype(float)

# Examine the distributions of the variables
print(data.describe())

# Identify patterns or trends
print(data.groupby('main_category')['no_of_ratings'].mean())

# Compute total sales for each main category and sub-category
total_sales = data.groupby(['main_category', 'sub_category'])[['discount_price']].sum()

# Compute average rating and number of ratings for each main category and sub-category
avg_ratings = data.groupby(['main_category', 'sub_category'])[['ratings', 'no_of_ratings']].mean()

# Compute average discount percentage for each main category and sub-category
avg_discount = (1 - (data['discount_price'] / data['actual_price'])).groupby(
    [data['main_category'], data['sub_category']]).mean() * 100

# Identify best-selling shoe in each main category and sub-category
best_selling = data.sort_values(by='no_of_ratings', ascending=False).groupby(['main_category', 'sub_category']).first()


# Plot total sales for each main category and sub-category
total_sales.plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.title('Total Sales by Category and Sub-Category')
plt.show()

# Create a scatterplot of average rating and number of ratings for each main category and sub-category
avg_ratings.plot(kind='scatter', x='ratings', y='no_of_ratings')
plt.xlabel('Average Rating')
plt.ylabel('Number of Ratings')
plt.title('Average Rating and Number of Ratings by Category and Sub-Category')
plt.show()

# Plot average discount percentage for each main category and sub-category
avg_discount.plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Average Discount Percentage')
plt.title('Average Discount Percentage by Category and Sub-Category')
plt.show()

# Show the best-selling shoe in each main category and sub-category
print(best_selling[['discount_price']])

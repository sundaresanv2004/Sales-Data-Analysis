import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Updated_Shoes.csv')

# Filtering columns
df = pd.DataFrame(data[['name', 'main_category', 'sub_category', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']])

# Check for missing values
# print(df.isnull().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Convert data types if necessary
df['discount_price'] = df['discount_price'].astype(float)
df['actual_price'] = df['actual_price'].astype(float)

# Examine the distributions of the variables
print()
# print(df.describe())

# Identify patterns or trends
a = df.groupby(['main_category', 'sub_category']).head()
print(a.to_string())

# Compute total sales for each main category and sub-category
total_sale = df.groupby(['main_category', 'sub_category'])[['discount_price']].sum()
# print(total_sale)
total_sales = data.groupby(['main_category', 'sub_category'])[['discount_price']].sum()


# Compute average rating and number of ratings for each main category and sub-category
avg_ratings = data.groupby(['main_category', 'sub_category'])[['ratings', 'no_of_ratings']].mean()

# Compute average discount percentage for each main category and sub-category
avg_discount = (1 - (data['discount_price'] / data['actual_price'])).groupby([data['main_category'], data['sub_category']]).mean() * 100


# Identify best-selling shoe in each main category and sub-category
best_selling = data.sort_values(by='no_of_ratings', ascending=False).groupby(['main_category', 'sub_category']).first()


# Step 5: Visualization
# Plot total sales for each main category and sub-category
# print(total_sales)
data.plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.title('Total Sales by Category and Sub-Category')
plt.show()

# Create a scatterplot of average rating and number of ratings for each main category and sub-category
#  print(avg_ratings)
#  data.plot(kind='scatter', x='ratings', y='no_of_ratings')
#  plt.xlabel('Average Rating')
#  plt.ylabel('Number of Ratings')
#  plt.title('Average Rating and Number of Ratings by Category and Sub-Category')
#  plt.show()
#
#  # Plot average discount percentage for each main category and sub-category
#  avg_discount.plot(kind='bar')
#  plt.xlabel('Category')
#  plt.ylabel('Average Discount Percentage')
#  plt.title('Average Discount Percentage by Category and Sub-Category')
#  plt.show()
#
#  # Show the best-selling shoe in each main category and sub-category
#  print()
#  # print(best_selling['discount_price'])
#
#  # Step 6: Conclusion
#  # Summarize your findings and draw conclusions based on your analysis
#
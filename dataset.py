import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tips_data = sns.load_dataset("tips")

print(tips_data.head())
print(tips_data.describe())

# Check for missing values
print(tips_data.isnull().sum())

# Visualize the data
sns.distplot(tips_data["total_bill"], label="Total Bill")
plt.legend()
plt.show()

sns.scatterplot(x="total_bill", y="tip", data=tips_data)
plt.show()

sns.boxplot(x="day", y="tip", data=tips_data)
plt.show()

# Clean the data
cleaned_data = tips_data.dropna()

# Replace missing values with the mean of the column
cleaned_data["total_bill"].fillna(cleaned_data["total_bill"].mean(), inplace=True)

# Create new variables
cleaned_data["tip_percentage"] = cleaned_data["tip"] / cleaned_data["total_bill"] * 100

# Calculate summary statistics
print(cleaned_data["tip_percentage"].mean())
print(cleaned_data["tip_percentage"].median())
print(cleaned_data["tip_percentage"].std())

# Explore relationships
sns.scatterplot(x="total_bill", y="tip_percentage", data=cleaned_data)
plt.show()

print(cleaned_data["total_bill"].corr(cleaned_data["tip_percentage"]))

# Summarize the findings
print("The average tip percentage is", cleaned_data["tip_percentage"].mean())
print("The median tip percentage is", cleaned_data["tip_percentage"].median())
print("The standard deviation of the tip percentage is", cleaned_data["tip_percentage"].std())
print("The correlation between total bill and tip percentage is", cleaned_data["total_bill"].corr(cleaned_data["tip_percentage"]))


 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset 
file_path = 'Titanic Dataset.xlsx'
df = pd.read_excel(file_path, sheet_name='Titanic')

# This stats can be obtained only for numerical columns
numerical_cols = ['Age', 'Family', 'Fare']

# Looping through each column and calculating statistics
for col in numerical_cols:
    print(f"
Statistics for {col}:")
    print(f"Mean: {df[col].mean()}")
    print(f"Median: {df[col].median()}")
    print(f"Mode: {df[col].mode().iloc[0]}")  # using .iloc[0] to avoid multiple modes
    print(f"Standard Deviation: {df[col].std()}")
    print(f"Variance: {df[col].var()}")
    print(f"Minimum: {df[col].min()}")
    print(f"Maximum: {df[col].max()}")
    print(f"Non-null Count: {df[col].count()}")

# Aggregating all the stats under one dataframe
stats = df[numerical_cols].agg(['mean', 'median', 'std', 'var', 'min', 'max', 'count']).T
stats['mode'] = df[numerical_cols].mode().iloc[0]

stats = stats.round(2)
print("
",stats)

#Checking for the null/missing values
print("
 Null values in each column:")
print( df.isnull().sum())

#Checking dtypes of each column
print(df.dtypes)


print(df['Survived'].value_counts())
print(df['Gender'].value_counts())
print(df['Pclass'].value_counts())

#Detection of distribution of data using histogram
for col in numerical_cols:
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.show()

# Box plot to detect outliers
for col in numerical_cols:
  sns.boxplot(x=df[col])
  plt.title(f'Boxplot of {col}')
  plt.show()

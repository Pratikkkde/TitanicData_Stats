# Exploratory Data Analysis (EDA) - Titanic Dataset
This project focuses on performing basic exploratory data analysis (EDA) to understand the structure, distribution, and relationships within the Titanic dataset. The main goal was to extract meaningful insights by analyzing data types, central tendencies, and variation in the dataset.

# Dataset Description 

Column | Description
Survived | Indicates whether the passenger survived (Yes/No)
Pclass | Passenger class (First, Second, Third)
Gender | Male or Female
Age | Age of the passenger
Family | Indicates if the passenger had family aboard
Embarked | Port of embarkation (start of the journey)

# Scope of Exploration

- Data Type Inspection
Checked and verified data types for each column to ensure accurate analysis.

- Central Tendency Measures
Mean, Median, and Mode were calculated for numerical features like Age.
Helped us understand the typical values and identify skewness.

- Measures of Dispersion
Standard Deviation and Variance provided insight into how spread out the data is, especially for Age.

- Value Counts & Categorical Distributions
Used frequency counts to explore categorical columns such as Survived, Pclass, Gender, and Embarked.
Helped us observe patterns and class distribution.

- Histograms for Data Distribution
Created histograms to visualize the distribution of numerical columns like Age.
Identified skewed data and spread across values.

- Box Plots for Outlier Detection
Used box plots to detect outliers in features like Age.
This helped us spot extreme values that could impact modeling and analysis.

- Relationships & Patterns
Explored how Survived relates to features like:
Gender: Females had a higher survival rate.
Pclass: First-class passengers showed better survival odds.
Family: Passengers with family had slightly higher survival rates.
Embarked: Some patterns were observed based on port of embarkation.

# Tools Used

Python: pandas, matplotlib, Seaborn, Numpy

# Conclusion

This EDA project served as a foundational step in understanding the Titanic dataset. By examining statistical properties, visual patterns, and feature relationships, we gained insights into survival trends and identified key influencing factors. This exploration sets the groundwork for future modeling or deeper hypothesis-driven analysis.

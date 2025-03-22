import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "API_SP.POP.TOTL_DS2_en_csv_v2_76253.csv"
df = pd.read_csv(file_path, encoding='latin1', skiprows=3)

# Select relevant columns
population_2023 = df[['Country Name', '2023']].dropna()

# Sort and get top 10 most populated countries
top_countries = population_2023.sort_values(by='2023', ascending=False).head(10)

# Plot bar chart
plt.figure(figsize=(12,6))
plt.bar(top_countries['Country Name'], top_countries['2023'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Population in 2023')
plt.title('Top 10 Most Populated Countries in 2023')
plt.xticks(rotation=45)
plt.show()

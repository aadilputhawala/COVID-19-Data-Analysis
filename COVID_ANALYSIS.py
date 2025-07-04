# COVID-19 Data Analysis Project using Pandas

import pandas as pd
import matplotlib.pyplot as plt

#  Load the dataset
df = pd.read_csv('covid_19_data.csv')  
#  Clean the data
df = df.rename(columns={
    'ObservationDate': 'Date',
    'Country/Region': 'Country',
    'Province/State': 'State',
    'Last Update': 'Last_Update',
    'Confirmed': 'Confirmed',
    'Deaths': 'Deaths',
    'Recovered': 'Recovered'
})

df['Date'] = pd.to_datetime(df['Date'])

# Handle missing values
df['State'] = df['State'].fillna('Unknown')
df[['Confirmed', 'Deaths', 'Recovered']] = df[['Confirmed', 'Deaths', 'Recovered']].fillna(0)

# Total confirmed cases by country
total_cases = df.groupby('Country')['Confirmed'].max().sort_values(ascending=False)

print("Top 5 Countries by Confirmed Cases:")
print(total_cases.head(10))

#  Bar plot for top 5 countries
top_5 = total_cases.head(5)
top_5.plot(kind='bar', color='skyblue')
plt.title('Top 5 Countries by Confirmed COVID-19 Cases')
plt.xlabel('Country')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#  Trend analysis for a specific country (e.g., India)
country = 'India'  
country_data = df[df['Country'] == country]

# Group by date
daily_trend = country_data.groupby('Date').sum(numeric_only=True)

# Line plot
daily_trend['Confirmed'].plot(figsize=(10, 5), color='green')
plt.title(f'COVID-19 Confirmed Cases in {country} Over Time')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.grid(True)
plt.tight_layout()
plt.show()

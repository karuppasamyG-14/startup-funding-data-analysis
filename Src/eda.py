import pandas as pd
import matplotlib.pyplot as plt

df_clean = pd.read_csv('../data/startup_clean.csv')
print(df_clean.columns)

top_cities = df_clean.groupby('CityLocation')['AmountInUSD'].sum().sort_values(ascending=False).head(10)
print(top_cities)

top_industries = df_clean.groupby('IndustryVertical')['AmountInUSD'].sum().sort_values(ascending=False).head(10)
print(top_industries)

yearly = df_clean.groupby('Year')['AmountInUSD'].sum()
print(yearly)

top_investors = df_clean['InvestorsName'].value_counts().head(10)
print(top_investors)

avg_by_type = df_clean.groupby('InvestmentnType')['AmountInUSD'].mean().sort_values(ascending = False).head(10)
print(avg_by_type)

plt.figure(figsize=(10,5))
top_cities.plot(kind='bar')
plt.title('Top 10 cities by Total Funding')
plt.xlabel('City')
plt.ylabel('Total Funding (USD)')
plt.tight_layout()
plt.savefig('../visualizations/top_cities.png')
plt.show()
plt.close()

plt.figure(figsize=(10,5))
yearly.plot(kind='line', marker='o')
plt.title('Startup Funding Trend by Year')
plt.ylabel('Total Funding (USD)')
plt.tight_layout()
plt.savefig('../visualizations/funding_trend.png')
plt.show()
plt.close()


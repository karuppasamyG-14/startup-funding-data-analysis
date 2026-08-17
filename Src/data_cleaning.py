import pandas as pd
df = pd.read_csv('../data/startup_funding.csv')
df = df.rename(columns={'Date dd/mm/yyyy' : 'Date'})
df = df.rename(columns={'Amount in USD' : 'Amount In USD' })
print(df.shape)
print(df.columns)
print(df.isnull().sum())

df.columns = df.columns.str.strip().str.replace(' ', '')

city_fix = {
    'Bengaluru': 'Bangalore',
    'bangalore': 'Bangalore',
    'Delhi': 'New Delhi',
    'gurgaon': 'Gurgaon',
    'Gurugram': 'Gurgaon'
}
df['CityLocation'] = df['CityLocation'].replace(city_fix)


df['AmountInUSD'] = df['AmountInUSD'].astype(str).str.replace(',', '')
df['AmountInUSD'] = pd.to_numeric(df['AmountInUSD'], errors='coerce')

df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)
df['Year'] = df['Date'].dt.year

df_clean = df.dropna(subset=['AmountInUSD'])

df_clean['CityLocation'] = df_clean['CityLocation'].str.strip().str.split('/').str[0]

df_clean.to_csv('startup_clean.csv', index=False)
print("Cleaned:", df_clean.shape)
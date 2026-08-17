import os
import pandas as pd
from sqlalchemy import create_engine

print("Step 1: Starting script")

username = 'root'
password = os.environ.get('MYSQL_PASSWORD')
host = 'localhost'
database = 'startup_funding'

try:
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')
    print("Step 2: Engine created")

    df_clean = pd.read_csv('../data/startup_clean.csv')
    print("Step 3: CSV loaded, shape:", df_clean.shape)

    df_clean.to_sql('startups', engine, if_exists='replace', index=False)
    print("Step 4: Data loaded into MySQL")

    result = pd.read_sql_query("SELECT COUNT(*) as cnt FROM startups", engine)
    print("Step 5: Row count in MySQL:", result)

    queries = {
        "Top 5 cities by funding": """
                                   SELECT CityLocation, SUM(AmountInUSD) as total
                                   FROM startups
                                   GROUP BY CityLocation
                                   ORDER BY total DESC LIMIT 5
                                   """,
        "Deals per year": """
                          SELECT `Year`, COUNT(*) as deals
                          FROM startups
                          GROUP BY `Year`
                          ORDER BY `Year`
                          """,
        "Top 10 city-industry combinations": """
                                 SELECT CityLocation, IndustryVertical, SUM(AmountInUSD) as total
                                 FROM startups
                                 GROUP BY CityLocation, IndustryVertical
                                 ORDER BY total DESC LIMIT 10
                                 """,
        "Top 10 most active investors": """
                                        SELECT InvestorsName, COUNT(*) as deals
                                        FROM startups
                                        GROUP BY InvestorsName
                                        ORDER BY deals DESC LIMIT 10
                                        """
    }

    for name, q in queries.items():
        print(f"\n--- {name} ---")
        print(pd.read_sql_query(q, engine))

except Exception as e:
    print("ERROR OCCURRED:", e)
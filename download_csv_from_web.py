import pandas as pd


url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

data = pd.read_csv(url)

data.to_csv("data/owid-covid-data.csv", compression='gzip', index=False)

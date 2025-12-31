import pandas as pd

articles = json_data["articles"]
df = pd.DataFrame(articles)

print(df.head())
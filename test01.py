import requests
import pandas as pd

url = "https://hn.algolia.com/api/v1/search_by_date"
params = {
    "query": "ai",
    "tags": "story"
}

response = requests.get(url, params=params)
json_data = response.json()



for article in json_data["hits"]:
    title = article.get("title")
    date = article.get("created_at")
    content = article.get("story_text")
    print(title, date)
    
    

articles = json_data["articles"]
df = pd.DataFrame(article)

print(df.head())
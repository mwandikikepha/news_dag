import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def getnews(query="tesla"):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={os.getenv('api_key')}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])
    df = pd.DataFrame(articles)
    print(f"Successfully fetched {len(df)} articles for {query}")
    print(df[['title', 'publishedAt','url']].head())
    
if __name__ == "__main__":
    getnews("tesla")

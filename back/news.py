import requests 

## 1355e0a8d61d40cd8436032d736c06f3

url = "https://newsapi.org/v2/everything"



def tickerNews(topic):
    query_params = {
        "q": topic,
        "from": "2026-06-25",
        "sortBy": "popularity",
        "apiKey": "1355e0a8d61d40cd8436032d736c06f3"
    }

    response = requests.get(url, params=query_params)
    data = response.json()
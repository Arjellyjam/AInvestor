import requests
from datetime import datetime, timedelta 


url = "https://finnhub.io/api/v1/company-news"



## CHANGE TO FINNHUB

def tickerNews(topic):

    today = datetime.today().strftime('%Y-%m-%d')
    three_days = (datetime.today() - timedelta(days=3)).strftime('%Y-%m-%d')

    query_params = {
        "symbol": topic,
        "from": three_days,
        "to": today,
        "token": "d9dmg41r01qui7p2rncgd9dmg41r01qui7p2rnd0"
        ## idrc
    }

    response = requests.get(url, params=query_params)
    # print(response.json())
    return(response.json())

import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key_stock = "0OKW4EZVCV1LBB8N"
api_key_news = "cf3c34c747434163b1df41a3e6fdb89a"

account_sid = "AC63e3c3da06430894226fdc6fa5e388be"
auth_token = "dd896d66a89d69dcf97a73d7622ad576"
client = Client(account_sid, auth_token)

per_change_increase = 0
per_change_decrease = 0

params_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key_stock
}

now = dt.datetime.now().date()
yesterday = str(now - dt.timedelta(days=1))
before_yesterday = str(now - dt.timedelta(days=2))

response_stock = requests.get(url=STOCK_ENDPOINT, params=params_stock)
response_stock.raise_for_status()
data_stock = response_stock.json()
yesterday_close_price = float(data_stock["Time Series (Daily)"][yesterday]["4. close"])
before_yesterday_close_price = float(data_stock["Time Series (Daily)"][before_yesterday]["4. close"])

if yesterday_close_price > before_yesterday_close_price:
    per_change_increase = round(((yesterday_close_price-before_yesterday_close_price)/before_yesterday_close_price) * 100,2)
else:
    per_change_decrease = round(((before_yesterday_close_price-yesterday_close_price)/before_yesterday_close_price) * 100,2)

params_news = {
    "qInTitle": COMPANY_NAME,
    "from": yesterday,
    "to": yesterday,
    "sortBy": "popularity",
    "apiKey": api_key_news,
    "pageSize": 3,
}

response_news = requests.get(url=NEWS_ENDPOINT, params=params_news)
response_news.raise_for_status()
data_news = response_news.json()

messages_list = []

if per_change_increase >=5:
    messages_list = [f'TSLA up {per_change_increase}%.\nHeadline: {data_news["articles"][article]["title"]}\nBrief: {data_news["articles"][article]["description"]}' for article in range(0,3)]
    for messages in messages_list:
            message = client.messages \
        .create(
                body=messages,
                from_='+18149046140',
                to='+48787943259'
            )
    
elif per_change_decrease >= 5:
    messages_list = [f'TSLA down {per_change_decrease}%.\nHeadline: {data_news["articles"][article]["title"]}\nBrief: {data_news["articles"][article]["description"]}' for article in range(0,3)]
    for messages in messages_list:
            message = client.messages \
        .create(
                body=messages,
                from_='+18149046140',
                to='+48787943259'
            )
        
else:
    print("TSLA price didn't change much")
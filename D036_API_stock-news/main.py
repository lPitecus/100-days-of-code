from datetime import datetime as dt
import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY = os.environ.get('STOCK_API_KEY')
STOCK_URL = "https://www.alphavantage.co/query"


def get_stock_diference() -> str:
    """Goes into the stock market to pull the prices of a certain company at close times in the
     last two days, compare them and returns the variation in percentage

     :return: str - the variation of the market value in the last 2 days"""
    parameters = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": STOCK,
        "interval": "60min",
        "outputsize": "compact",
        "apikey": STOCK_API_KEY
    }
    response = requests.get(url=STOCK_URL, params=parameters)
    response.raise_for_status()

    data = response.json()
    day_yesterday = int(dt.now().day) - 1
    day_before_yesterday = int(dt.now().day) - 2
    # Putting the values of yesterday and the bay before yesterday in a datetime object
    # and converting that object into a string
    date_yesterday = str(dt(int(dt.now().year), int(dt.now().month), day_yesterday).date())
    date_before_yesterday = str(dt(int(dt.now().year), int(dt.now().month), day_before_yesterday).date())

    # getting the value when the market closed yesterday at 16:00
    yesterday_close_value = float(data["Time Series (60min)"][f"{date_yesterday} 16:00:00"]["4. close"])

    # getting the value when the market closed the day before yesterday at 16:00
    before_yesterday_close_value = float(data["Time Series (60min)"][f"{date_before_yesterday} 16:00:00"]["4. close"])

    diference = round((((yesterday_close_value/before_yesterday_close_value)-1)*100), 2)
    if diference >= 0:
        return f"🔺{diference}%"
    if diference <= 0:
        return f"🔻{diference}%"


def get_articles_to_text() -> str:
    """Gets the first 3 news articles from the web, treats them
     and puts the content into a string with the title and the url for the site

     :return: str - String with all the articles and the respective links for them"""
    news_api_key = os.environ.get('NEWS_API_KEY')
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": news_api_key
    }
    news_response = requests.get(url="https://newsapi.org/v2/top-headlines", params=news_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()
    news_list: list = news_data["articles"][:3]
    news_dict = {item['title']: item['url'] for item in news_list}
    text = []
    for item in news_dict:
        text.append(f"{item}\n")
        text.append(f"{news_dict[item]}\n")

    msg = " ".join(text)
    return msg


def send_message(msg_txt: str):
    """Sends a text to my number

    :param msg_txt: str - Message to be sent
    """
    account_sid = os.environ.get('SID')
    auth_token = os.environ.get('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"\n{STOCK}: {get_stock_diference()}\n\n{msg_txt}",
                         from_='+12567334078',
                         to='+5584991341278'
                     )

    print(message.sid)


articles = get_articles_to_text()
print(articles)
send_message(articles)

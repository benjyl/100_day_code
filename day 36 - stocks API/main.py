import requests
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = "GEYAARSPLFH33ZOM"
NEWS_API_KEY = "e34b87adedb044b7a6340bc1aa0bc78c"

MY_EMAIL = "jstew613@gmail.com"
PASSWORD = "ioylffhmzmwwrmnq"
RECIP_EMAIL = "benjy.lovat@gmail.com"

today = datetime.today()
yesterday = today - timedelta(days=1)
# print(yesterday)
date_list = [str(yesterday.date() - timedelta(days=x)) for x in range(20)]
# print(date_list)


def get_news(date):
    """_summary_

    Args:
        date (string): get current date

    Returns:
        news_titles(list), news_urls(list): list of both main stories and urls for company7
    """
    news_url = (
        "https://newsapi.org/v2/everything?"
        f"q={COMPANY_NAME}&"
        "searchIn=title,description&"
        f"from={date}&"
        f"to={date}&"
        "sortBy=popularity&"
        "apiKey=e34b87adedb044b7a6340bc1aa0bc78c"
    )
    news_response = requests.get(news_url)
    news_response.raise_for_status()
    news_data = news_response.json()
    news = news_data["articles"][:3]  # get first 3 articles
    print(news)
    # for article in news:
    #     title = article["title"]
    #     # content = article["description"]
    #     print(title)
    news_titles = [article["title"] for article in news]
    news_urls = [article["url"] for article in news]
    return news_titles, news_urls


def stock_change(data, current_day, prev_day):
    """_summary_

    Args:
        data (json): stock json data
        current_day (string): current day
        prev_day (string): previous day

    Returns:
        percent_change (float): % diff in stock price between 2 days
    """
    day_close_price = float(data[f"{current_day}"]["4. close"])
    prev_day_close_price = float(data[f"{prev_day}"]["4. close"])
    percent_change = (
        (day_close_price - prev_day_close_price) / prev_day_close_price * 100
    )
    return percent_change


def send_message(news_titles, urls, diff):
    """_summary_

    Args:
        news_titles (list): news articles list
        urls (list): news urls list
        diff (float): stock percentage change between 2 days
    """
    if diff > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"
    message = MIMEText(
        f"TSLA: {up_down}{round(percent_change,1)}%\n{news_titles[0]}: {urls[0]}\n{news_titles[1]}: {urls[1]}\n{news_titles[2]}: {urls[2]}"
    )
    message["subject"] = "Tesla stock update"
    message["from"] = MY_EMAIL
    message["To"] = RECIP_EMAIL

    with smtplib.SMTP(
        "smtp.gmail.com", 587
    ) as connection:  # 587 - port number to successfully connect for email
        connection.starttls()  # tls (transport layer security-secure connection to email server)
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=RECIP_EMAIL, msg=message.as_string()
        )


# get stocks data
stocks_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={ALPHAVANTAGE_API_KEY}"
r = requests.get(stocks_url)
data = r.json()["Time Series (Daily)"]
print(data)

for i in range(len(date_list) - 1):
    try:
        curr_date = date_list[i]  # current day
        prev_date = date_list[i + 1]
        percent_change = stock_change(data, curr_date, prev_date)

        # percenteage change in stocks
        print(f"{curr_date}: {percent_change}")

        if abs(percent_change) > 5:
            # print(news_response.json())
            print("news")
            news_titles, urls = get_news(curr_date)
            print(news_titles)

            send_message(news_titles, urls, percent_change)

    except KeyError:
        print(f"No trading data for {date_list[i]}")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

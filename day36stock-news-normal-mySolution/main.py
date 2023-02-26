import requests
import datetime
from twilio.rest import Client

account_sid = "AC29b90230f83ecb2ec40116cb5de7e16c"
auth_token = "099104ede72c293d42b7c5aba809853b"

api_key_alpha = "IKBOZAVW70WNDM7W"
api_key_news = '83f635bd484d4459af398536caa3ab3c'


STOCK_NAME = "Apple"
COMPANY_NAME = "Apple"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response1 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=IKBOZAVW70WNDM7W")
date1 = (datetime.datetime.now()-datetime.timedelta(days = 1)).date()
data1 = float(response1.json()['Time Series (Daily)'][f"{date1}"]["4. close"])






#TODO 2. - Get the day before yesterday's closing stock price
date2 = (datetime.datetime.now()-datetime.timedelta(days = 2)).date()
data2 = float(response1.json()['Time Series (Daily)'][f"{date2}"]["4. close"])


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = abs(data1-data2)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
p_diff = round(diff*100/data2)

if data1 > data2:
    p_diff = f"🔺{p_diff}%"
else:
    p_diff = f"🔻{p_diff}%"


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

response2 = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey=83f635bd484d4459af398536caa3ab3c")
data3 = response2.json()['articles'][0]['title']
news = []
for i in range (0,3):
    news.append(f"{STOCK_NAME}{p_diff}\nHeadline : {response2.json()['articles'][i]['title']}\nBrief :{response2.json()['articles'][i]['description']}")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{news[i]}️",
        from_='+16812532298',
        to='+919135989874'

    )
    print(message.status)

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


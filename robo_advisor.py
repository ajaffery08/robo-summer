import os
from dotenv import load_dotenv
import requests

load_dotenv()

symbol = "MSFT" #ask for user input
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"

response = requests.get(request_url)
print(type(response))
print(response.text)
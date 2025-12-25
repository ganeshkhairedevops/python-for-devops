import requests
API_KEY = "G1JIHGMXW0J5CJLN"  # Step 1: Get API key
api_url = "https://www.alphavantage.co/"  # Step 2: Find a base URL




#print(api_url + query)

def get_stock_market_data(symbol):
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(api_url + query)
    print(response.json())

symbol = input("Enter stock name eg. (AMZN, GOGL, IBM,): ")
get_stock_market_data(symbol)
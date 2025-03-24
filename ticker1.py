#Tyson Blatter 2-22-25 8.1
#This lists the stocks and their price

stocks = {
    "APPL": 165.43,
    "MSFT": 135.76,
    "AAPL": 199.21,
    "GOOGL": 453.89,
    "AMZN" : 153.22,
    "TSLA" : 78.33,
    "META" : 333.56,
    "NVDA" : 1000.12,
    "NFLX" : 12.89,
    "DIS" : 92.15,
}

#ticker is used to help users find stock price upper is used to help find the ticker symbol easier
ticker = input("Enter the ticker symbol: ").upper()

#we create an if else code since they might input something that doesn't exist in our code
if ticker in stocks:
    print(f"The stock price for {ticker} is: {stocks[ticker]}")
else:
    print(f"Sorry, the stock price for {ticker} isn't available.")
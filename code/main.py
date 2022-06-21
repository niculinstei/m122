import string
from pip import main


def apiRequest():

    nowRequest = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=CHF").json()

    historyRequest = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=CHF&days=7&interval=daily").json()

    price = nowRequest["bitcoin"]["chf"]

    name = "Bitcoin"

    history = int(historyRequest["prices"][0][1])

    percentage = (price - history) / history * 100

    return price, name, history, percentage



def printThat(input):
    print(input)

def main():
    printThat("moin")


main()
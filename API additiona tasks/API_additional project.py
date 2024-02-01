import requests

def getting_price_eur_usd():
    url = "https://www.freeforexapi.com/api/live?pairs=EURUSD"

    try:
        response = requests.get(url)
        data = response.json()          #wanting json format for the answer
        rate = data['rates']['EURUSD']['rate']      #calling specific parts/format from the jsn document
        return rate

        # print(data)     #this way prints the complete information from the defined json in the API

    except requests.exceptions.RequestException as e:           #catching mistakes if any, so the function does not crash
        print('Error')


currency_rate = getting_price_eur_usd()
print(currency_rate)
import requests
import sys
import json

'''

In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy.
    If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.

Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
    which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
    Be sure to catch any exceptions, as with code like:
        import requests

        try:
            ...
        except requests.RequestException:
            ...
Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.


'''

def main():
    if len(sys.argv) != 2:
        sys.exit('Miss command-line agrument')
    else:
        try:
            num = float(sys.argv[1])
            print(f'{num}')
        except ValueError:
             sys.exit('Command-line agrument is not a number')
        else:
            amount = get_dollars() * num
            print(f"${amount:,.4f}")

def get_dollars():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        # print(json.dumps(response.json(), indent=2))
        json_output = response.json()
        # print(json_output['bpi']['USD']['rate_float'])
        return json_output['bpi']['USD']['rate_float']

    except requests.RequestException:
        print('incorrect')


if __name__ == "__main__":
    main()


# check50 cs50/problems/2022/python/bitcoin
# submit50 cs50/problems/2022/python/bitcoin
# pip install requests
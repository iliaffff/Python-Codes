import requests

user_bitcoin = float(input("How many bitcoins you want to buy? "))
MY_API_KEY = "48b02e70e213fef2ca37b1b2dae0619780c6ac068488ace6cd66c185764601e1"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={MY_API_KEY}"

response = requests.get(url).json()
dollar = response["data"]["priceUsd"]
cost = user_bitcoin * float(dollar)


print(f"{user_bitcoin} Bitcoins costs ${cost}")

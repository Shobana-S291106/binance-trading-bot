from binance.client import Client
from config import API_KEY, API_SECRET

# Enable Testnet Mode
client = Client(API_KEY, API_SECRET, testnet=True)

# Futures Testnet URL
client.FUTURES_URL = "https://testnet.binancefuture.com"

try:
    account = client.futures_account()
    print("✅ Connected Successfully!")
    print("Balance:", account["totalWalletBalance"])

except Exception as e:
    print("❌ Connection Failed")
    print(e)
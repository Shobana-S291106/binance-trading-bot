import argparse
import logging

from client.binance_client import BinanceFuturesClient
from logger import setup_logger


def main():

    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        client = BinanceFuturesClient()

        print("\n--- Order Details ---")
        print("Symbol:", args.symbol)
        print("Side:", args.side)
        print("Type:", args.type)
        print("Quantity:", args.quantity)
        print("Price:", args.price)

        response = client.place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n--- Order Result ---")
        print("Order ID:", response["orderId"])
        print("Status:", response["status"])
        print("Executed:", response["executedQty"])

        print("\n✅ Success!")

    except Exception as e:

        print("\n❌ Error")
        print(e)


if __name__ == "__main__":
    main()
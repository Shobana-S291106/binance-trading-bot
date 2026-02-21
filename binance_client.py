from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL
import logging


class BinanceFuturesClient:
    """
    Handles all communication with Binance Futures Testnet
    """

    def __init__(self):

        # Connect to Binance Testnet
        self.client = Client(API_KEY, API_SECRET, testnet=True)

        # Set Futures Testnet URL
        self.client.FUTURES_URL = BASE_URL

        # Logger
        self.logger = logging.getLogger()

        self.logger.info("Binance Futures Client Initialized")

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: float = None
    ):
        """
        Place Market or Limit order on Futures Testnet
        """

        try:

            self.logger.info("Preparing order")

            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            # Add price for LIMIT orders
            if order_type.upper() == "LIMIT":

                if price is None:
                    raise ValueError("Price is required for LIMIT order")

                params["price"] = price
                params["timeInForce"] = "GTC"

            self.logger.info(f"Order Params: {params}")

            # Send order
            response = self.client.futures_create_order(**params)

            self.logger.info(f"Order Response: {response}")

            return response

        except Exception as e:

            self.logger.error(f"Order Failed: {str(e)}")
            raise
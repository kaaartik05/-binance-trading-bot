# bot.py

import yfinance as yf
from datetime import datetime


class BasicBot:
    def __init__(self, api_key, api_secret, logger):
        self.api_key = api_key
        self.api_secret = api_secret
        self.logger = logger
        self.logger.info(" Bot initialized with mock API (yfinance)")

    def get_price(self, symbol):
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1d")
            price = hist["Close"].iloc[-1]
            return round(price, 2)
        except Exception as e:
            self.logger.error(f" Failed to fetch price: {str(e)}")
            return None

    def place_order(self, symbol, side, order_type, quantity, price=None):
        live_price = self.get_price(symbol)
        if live_price is None:
            self.logger.error(" Order failed: could not fetch live price.")
            return None

        executed_price = live_price if order_type == "market" else price
        order = {
            "symbol": symbol,
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
            "executed_price": executed_price,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "FILLED"
        }

        self.logger.info(f" Order Placed: {order}")
        return order

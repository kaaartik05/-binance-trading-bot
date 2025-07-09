# main.py

from bot import BasicBot
from config import API_KEY, API_SECRET
from logger import setup_logger
from cli import get_user_input


def main():
    logger = setup_logger()
    print(" Welcome to the Binance Futures Testnet Bot (Simulated)")

    symbol, side, order_type, quantity, price = get_user_input()

    print("\nPlacing order... ⏳\n")
    bot = BasicBot(API_KEY, API_SECRET, logger)
    result = bot.place_order(symbol, side, order_type, quantity, price)

    if result:
        print(f" Order executed: {result}")
    else:
        print(" Order failed. Check logs for more info.")


if __name__ == "__main__":
    main()

# cli.py

def get_user_input():
    symbol = input("Enter trading pair (e.g., BTC-USD): ").strip()
    side = input("Buy or Sell? (buy/sell): ").strip().lower()
    order_type = input("Order type (market/limit): ").strip().lower()
    quantity = float(input("Quantity to trade: ").strip())

    price = None
    if order_type == "limit":
        price = float(input("Enter limit price: ").strip())

    return symbol, side, order_type, quantity, price

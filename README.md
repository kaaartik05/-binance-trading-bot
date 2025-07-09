# Binance Trading Bot (Simulated with yFinance)

This is a mock trading bot built as part of a hiring challenge for the role of Junior Python Developer – Crypto Trading Bot.  
It simulates placing market and limit orders in a Binance-style environment using the `yfinance` library for live crypto price data.  
The bot follows a modular Python structure, accepts command-line input, and logs all activities and errors.

## Features

- Simulated market and limit order placement
- Buy and sell order support
- Command-line interface for real-time input
- Live price data via yFinance (Yahoo Finance API)
- Structured logging of orders and errors in `bot.log`
- Modular codebase: `bot.py`, `cli.py`, `config.py`, `logger.py`, and `main.py`

## Why Binance API Was Not Used

Due to ongoing issues with accessing the Binance Futures Testnet API (such as unavailable API key generation and lack of permissions),  
this project uses the `yfinance` library as a drop-in simulation layer.  
The bot structure, functionality, and CLI behavior remain fully aligned with the original assignment requirements, ensuring realism without dependency issues.

## Files Included

- `bot.py` – Core logic for placing simulated orders
- `cli.py` – Command-line interface for user input
- `config.py` – Stores mock API credentials
- `logger.py` – Logging setup
- `main.py` – Program entry point
- `bot.log` – Log file capturing all order attempts

## How to Run

1. Install dependencies:
   ```bash
   pip install yfinance

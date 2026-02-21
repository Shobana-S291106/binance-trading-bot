# Binance Futures Testnet Trading Bot

## Description
A Python CLI-based trading bot that places Market and Limit orders
on Binance Futures Testnet (USDT-M).

## Setup
1. Create Binance Testnet account
2. Generate API keys
3. Add keys in config.py
4. Install dependencies

```bash
pip install -r requirements.txt
Run Examples
Market Order
python -m cli.main --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003
Limit Order
python -m cli.main --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.003 --price 60000
Features

Market and Limit orders

CLI interface

Logging

Error handling

Modular structure

Author

Shobana S
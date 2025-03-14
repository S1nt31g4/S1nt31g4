import ccxt

exchange = ccxt.binance()
ticker = exchange.fetch_ticker('BTC/USDT')

print(f"Precio actual de BTC/USDT: {ticker['last']}")

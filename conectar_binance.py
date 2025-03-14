import ccxt  # Importamos la biblioteca ccxt

# Conectar con Binance
exchange = ccxt.binance()

# Obtener información general del exchange
exchange_info = exchange.fetch_markets()

# Imprimir información sobre el mercado de Binance
print(f"✅ Conectado a {exchange.name}")
print(f"🔹 Número de mercados disponibles: {len(exchange_info)}")
print(f"🔹 Monedas soportadas: {[market['symbol'] for market in exchange_info[:10]]}...")  # Mostramos solo 10

import ccxt  # Importamos la biblioteca ccxt

# Obtener la lista de todos los exchanges soportados
exchanges = ccxt.exchanges

# Imprimir la cantidad de exchanges disponibles
print(f"✅ Total de exchanges disponibles: {len(exchanges)}")

# Imprimir la lista de exchanges
for exchange in exchanges:
    print(exchange)

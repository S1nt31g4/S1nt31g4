import ccxt  # Importamos la biblioteca ccxt

# Obtener la lista de todos los exchanges disponibles
exchange_names = ccxt.exchanges

# Diccionario para almacenar las conexiones
exchanges = {}

print(f"✅ Conectando con {len(exchange_names)} exchanges...\n")

# Conectar a cada exchange automáticamente
for name in exchange_names:
    try:
        exchange_class = getattr(ccxt, name)  # Obtiene la clase del exchange
        exchanges[name] = exchange_class()  # Instancia el exchange
        print(f"✅ Conectado a {name}")
    except Exception as e:
        print(f"❌ No se pudo conectar a {name}: {str(e)}")

# Mostrar cuántos exchanges logramos conectar
print(f"\n✅ Total de exchanges conectados: {len(exchanges)}")

import ccxt  # Importamos la biblioteca ccxt

# Obtener la lista de todos los exchanges disponibles
exchange_names = ccxt.exchanges

# Lista para almacenar los datos
data = []

print(f"✅ Conectando con {len(exchange_names)} exchanges...\n")

# Conectar y obtener precios
for name in exchange_names:
    print(f"🔹 Intentando conectar con {name}...")  # Mensaje de depuración
    try:
        exchange_class = getattr(ccxt, name)  # Obtener la clase del exchange
        exchange = exchange_class()  # Instanciar el exchange
        print(f"✅ Conectado a {name}")  # Confirmación de conexión
        
        ticker = exchange.fetch_ticker('BTC/USDT')  # Obtener el precio
        data.append({"Exchange": name, "Precio": ticker['last']})

        print(f"💰 {name}: ${ticker['last']}")  # Mostrar precio obtenido
    except Exception as e:
        print(f"❌ {name} - Error: {str(e)}")

# Mostrar total de precios obtenidos
print(f"\n✅ Total de precios obtenidos: {len(data)}")

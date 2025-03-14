import ccxt  # Importamos la biblioteca ccxt

# Obtener la lista de todos los exchanges disponibles
exchange_names = ccxt.exchanges

# Lista para almacenar los datos
data = []
errores = []
exchanges_validos = []

print(f"✅ Conectando con {len(exchange_names)} exchanges...\n")

# Conectar y obtener precios
for name in exchange_names:
    print(f"🔹 Intentando conectar con {name}...", end=" ")  # Mantiene todo en una línea
    try:
        exchange_class = getattr(ccxt, name)  # Obtener la clase del exchange
        exchange = exchange_class()  # Instanciar el exchange
        
        # Verificar si el exchange tiene el par BTC/USDT antes de intentar obtener datos
        markets = exchange.load_markets()
        if 'BTC/USDT' not in markets:
            print("❌ No tiene BTC/USDT")
            errores.append({"Exchange": name, "Error": "No tiene BTC/USDT"})
            continue  # Salta al siguiente exchange

        # Obtener el precio
        ticker = exchange.fetch_ticker('BTC/USDT')
        data.append({"Exchange": name, "Precio": ticker['last']})
        exchanges_validos.append(name)

        print(f"💰 ${ticker['last']}")  # Mostrar precio obtenido

    except Exception as e:
        print(f"❌ Error")
        errores.append({"Exchange": name, "Error": str(e)})

# Mostrar resumen final
print(f"\n✅ Total de exchanges con datos válidos: {len(exchanges_validos)}")
print(f"❌ Exchanges con errores o sin BTC/USDT: {len(errores)}")

# Mostrar lista de exchanges exitosos
if exchanges_validos:
    print("\n📌 Exchanges con precios correctos:")
    for exchange in exchanges_validos:
        print(f"   - {exchange}")

# Mostrar lista de exchanges con errores
if errores:
    print("\n🚨 Exchanges con problemas:")
    for error in errores[:10]:  # Mostrar solo los primeros 10 para no saturar la consola
        print(f"   - {error['Exchange']}: {error['Error']}")


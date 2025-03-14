import ccxt
import csv
import datetime

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

        # Verificar si el exchange tiene el par BTC/USDT
        markets = exchange.load_markets()
        if 'BTC/USDT' not in markets:
            print("❌ No tiene BTC/USDT")
            errores.append({"Exchange": name, "Error": "No tiene BTC/USDT"})
            continue  # Salta al siguiente exchange

        # Obtener el precio
        ticker = exchange.fetch_ticker('BTC/USDT')
        precio = ticker['last']

        # Guardar los datos en la lista
        data.append({"Exchange": name, "Precio": precio, "Fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        exchanges_validos.append(name)

        print(f"💰 ${precio}")  # Mostrar precio obtenido

    except Exception as e:
        print(f"❌ Error")
        errores.append({"Exchange": name, "Error": str(e)})  # ✅ Aquí está corregido el error de sintaxis

# Guardar los datos en un archivo CSV
csv_filename = f"precios_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ["Exchange", "Precio", "Fecha"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

print(f"\n✅ Los datos han sido guardados en el archivo: {csv_filename}")

# Mostrar resumen final
print(f"\n✅ Total de exchanges con datos válidos: {len(exchanges_validos)}")
print(f"❌ Exchanges con errores o sin BTC/USDT: {len(errores)}")

if exchanges_validos:
    print("\n📌 Exchanges con precios correctos:")
    for exchange in exchanges_validos:
        print(f"   - {exchange}")

if errores:
    print("\n🚨 Exchanges con problemas:")
    for error in errores[:10]:  # Mostrar solo los primeros 10 errores para no saturar la consola
        print(f"   - {error['Exchange']}: {error['Error']}")

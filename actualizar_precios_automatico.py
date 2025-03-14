import time
import ccxt
import csv
import datetime

def obtener_precios():
    exchange_names = ccxt.exchanges
    data = []
    errores = []
    exchanges_validos = []

    print(f"\n⏳ Actualizando precios... ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")

    for name in exchange_names:
        try:
            exchange_class = getattr(ccxt, name)
            exchange = exchange_class()

            markets = exchange.load_markets()
            if 'BTC/USDT' not in markets:
                errores.append({"Exchange": name, "Error": "No tiene BTC/USDT"})
                continue

            ticker = exchange.fetch_ticker('BTC/USDT')
            precio = ticker['last']

            data.append({"Exchange": name, "Precio": precio, "Fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            exchanges_validos.append(name)

            print(f"✅ {name}: ${precio}")

        except Exception as e:
            errores.append({"Exchange": name, "Error": str(e)})

    # Guardar los datos en CSV
    csv_filename = f"precios_actualizados.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["Exchange", "Precio", "Fecha"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"\n✅ Datos guardados en {csv_filename}")
    print(f"✅ Total de exchanges con datos válidos: {len(exchanges_validos)}")
    print(f"❌ Exchanges con errores o sin BTC/USDT: {len(errores)}\n")

# 🚀 Ejecutar el script cada 5 minutos (300 segundos)
while True:
    obtener_precios()
    print("🔄 Esperando 5 minutos para la próxima actualización...\n")
    time.sleep(300)  # Espera 300 segundos (5 minutos) antes de volver a ejecutar

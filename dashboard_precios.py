import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
import ccxt
import threading
import time

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Lista de exchanges a monitorear
exchange_names = ["binance", "kraken", "coinbase", "kucoin", "okx"]

# Datos iniciales
data = []

# Función para obtener precios en tiempo real
def actualizar_precios():
    global data
    while True:
        temp_data = []
        for name in exchange_names:
            try:
                exchange_class = getattr(ccxt, name)
                exchange = exchange_class()
                ticker = exchange.fetch_ticker('BTC/USDT')
                precio_actual = ticker['last']
                temp_data.append({"Exchange": name, "Precio": precio_actual})
            except Exception as e:
                print(f"❌ Error en {name}: {str(e)}")
        
        if temp_data:
            data = temp_data  # Actualizar la variable global con nuevos datos
        time.sleep(30)  # Actualizar cada 30 segundos

# Iniciar la actualización de precios en un hilo separado
hilo = threading.Thread(target=actualizar_precios)
hilo.daemon = True
hilo.start()

# Layout del Dashboard
app.layout = html.Div([
    html.H1("📈 Dashboard de Precios de BTC/USDT en Tiempo Real"),
    html.P("Actualización automática cada 30 segundos"),
    dcc.Graph(id="grafico-precios"),
    dcc.Interval(
        id="intervalo-actualizacion",
        interval=30000,  # 30 segundos
        n_intervals=0
    )
])

# Callback para actualizar el gráfico en tiempo real
@app.callback(
    dash.Output("grafico-precios", "figure"),
    dash.Input("intervalo-actualizacion", "n_intervals")
)
def actualizar_grafico(n):
    if not data:
        return go.Figure()

    df = pd.DataFrame(data)
    fig = go.Figure([go.Bar(x=df["Exchange"], y=df["Precio"], text=df["Precio"], textposition="auto")])
    fig.update_layout(title="Precios de BTC/USDT en Exchanges", xaxis_title="Exchanges", yaxis_title="Precio")
    return fig

# Ejecutar el Dashboard
if __name__ == "__main__":
    app.run_server(debug=True)

import yfinance as yf
import pandas as pd

print("⏳ Descargando futuro continuo del oro (GC=F)...")

# Descargar desde 2000
oro_raw = yf.download(
    "GC=F",
    start="2000-01-01",
    auto_adjust=True,
    progress=False
)

if oro_raw.empty:
    raise ValueError("⚠️ No se pudieron descargar datos del oro.")

# Manejo correcto del MultiIndex
if isinstance(oro_raw["Close"], pd.DataFrame):
    precio = oro_raw["Close"].iloc[:, 0]
else:
    precio = oro_raw["Close"]

# Construir DataFrame limpio
df = pd.DataFrame({
    "fecha": precio.index,
    "precio_usd": precio.values
})

# Calcular variación diaria %
df["variacion_pct"] = df["precio_usd"].pct_change() * 100

# Limpiar y ordenar
df = df.dropna().sort_values("fecha")

# Guardar archivo
df.to_csv("Oro_historico_2000.csv", index=False, encoding="utf-8")

print(f"✅ Archivo generado correctamente con {len(df)} registros.")
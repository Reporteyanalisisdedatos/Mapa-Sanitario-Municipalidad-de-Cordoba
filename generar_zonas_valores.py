import pandas as pd

try:
    # Cargar el archivo original
    df = pd.read_csv("data/Vista_2022AreasProgramaticas.csv", encoding="utf-8")

    # Convertir columna Zona a numérico (por seguridad)
    df["Zona"] = pd.to_numeric(df["Zona"], errors="coerce")

    # Agrupar y sumar por Zona
    agrupado = df.groupby("Zona")[[
        "PoblacionTotal", "Mujeres", "Varones",
        "Hogares", "HogaresNBI", "PoblacionSinCobertura"
    ]].sum().reset_index()

    # Guardar como CSV
    agrupado.to_csv("data/zonas_valores.csv", index=False, encoding="utf-8")

    print("✅ Archivo zonas_valores.csv generado con \u00e9xito.")
except Exception as e:
    print("❌ Error:", e)


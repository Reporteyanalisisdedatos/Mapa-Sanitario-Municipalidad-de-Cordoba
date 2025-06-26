from fastapi import APIRouter
import pandas as pd
import json
from pathlib import Path

router = APIRouter()

@router.get("/api/efectores")
def efectores():
    try:
        base_path = Path(__file__).parent / "../data"
        centros_path = base_path / "Vista_CentrosHorarios.csv"
        areas_path = base_path / "Vista_2022AreasProgramaticas.csv"

        # Leer CSVs
        centros = pd.read_csv(centros_path, encoding="utf-8")
        areas = pd.read_csv(areas_path, encoding="utf-8")

        # Limpiar y convertir el porcentaje
        areas["PorcentajeSinCobertura"] = (
            areas["PorcentajeSinCobertura"]
            .astype(str)
            .str.replace("%", "")
            .str.strip()
            .replace("nan", pd.NA)
            .astype(float)
        )

        # Merge por 'Id'
        df = pd.merge(centros, areas, on="Id", how="left")

        # Construir FeatureCollection
        features = []
        for _, row in df.iterrows():
            if pd.isna(row.Latitud) or pd.isna(row.Longitud):
                continue

            try:
                lon = float(row.Longitud)
                lat = float(row.Latitud)
            except:
                continue

            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat],
                },
                "properties": {
                    "centro": row.Centro,
                    "institucion": row.get("institucion"),
                    "tipo": row.get("Tipo"),
                    "direccion": row.get("Direccion"),
                    "horario": row.get("Horario"),
                    "zona": row.get("Zona"),
                    "poblacion": row.get("PoblacionTotal"),
                    "varones": row.get("Varones"),
                    "mujeres": row.get("Mujeres"),
                    "hogares": row.get("Hogares"),
                    "hogares_nbi": row.get("HogaresNBI"),
                    "sin_cobertura": row.get("PoblacionSinCobertura"),
                    "porcentaje_sin_cobertura": row.get("PorcentajeSinCobertura"),
                },
            }
            features.append(feature)

        return {"type": "FeatureCollection", "features": features}

    except Exception as e:
        print(f"Error en /api/efectores: {e}")
        return {"error": str(e)}

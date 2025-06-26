from fastapi import APIRouter
import json
import pandas as pd
from pathlib import Path

router = APIRouter()

@router.get("/api/zonas-con-datos")
def zonas_con_datos():
    try:
        base_path = Path(__file__).parent.parent / "data"
        geojson_path = base_path / "ZONA.json"
        valores_path = base_path / "zonas_valores.csv"

        with open(geojson_path, encoding="utf-8") as f:
            geojson = json.load(f)

        df = pd.read_csv(valores_path)
        df = df.set_index("Zona")

        for feature in geojson["features"]:
            nombre = feature["properties"].get("name", "")
            zona_id_str = nombre.replace("ZONA ", "").strip()
            zona_id = int(zona_id_str) if zona_id_str.isdigit() else None

            if zona_id and zona_id in df.index:
                row = df.loc[zona_id]
                feature["properties"].update({
                    "poblacion": row["PoblacionTotal"],
                    "mujeres": row["Mujeres"],
                    "varones": row["Varones"],
                    "hogares": row["Hogares"],
                    "hogares_nbi": row["HogaresNBI"],
                    "cobertura": row["PoblacionSinCobertura"]
                })

        return geojson

    except Exception as e:
        return {"error": str(e)}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import endpoints.efectores_from_csv as efectores
import endpoints.zonas_from_csv as zonas

app = FastAPI(
    title="API Mapa CSV",
    description="Sirve datos de efectores y zonas desde archivos CSV/JSON",
    version="1.0.0"
)

# Permitir CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(efectores.router)
app.include_router(zonas.router)

# Ruta raíz para testeo
@app.get("/")
def root():
    return {"mensaje": "✅ API Mapa CSV activa"}



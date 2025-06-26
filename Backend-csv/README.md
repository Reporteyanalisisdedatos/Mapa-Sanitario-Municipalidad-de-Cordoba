# API Mapa CSV

Esta API sirve datos geoespaciales desde archivos CSV y JSON sin necesidad de base de datos.

## Cómo ejecutar

1. Crear entorno virtual (opcional):
```bash
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecutar servidor:
```bash
python -m uvicorn main:app --reload
```

4. Probar en el navegador:
- http://localhost:8000/docs
- http://localhost:8000/api/efectores
- http://localhost:8000/api/zonas-con-datos

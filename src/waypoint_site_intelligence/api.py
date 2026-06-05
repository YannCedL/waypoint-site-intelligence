# API FastAPI pour le moteur Waypoint Site Intelligence & Cadastre
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .cadastre import query_parcel

app = FastAPI(
    title="Waypoint Site Intelligence API",
    description="Moteur d'Intelligence Cadastrale & Parcelles IGN",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert directement la page d'accueil interface cadastre
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Waypoint API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Waypoint", "version": "1.0.0"}

@app.get("/api/v1/parcel", response_model=ResultContract)
def get_parcel(lat: float = Query(48.8566), lon: float = Query(2.3522)):
    return query_parcel(lat, lon)

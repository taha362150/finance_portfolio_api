from fastapi import FastAPI
from app.api.client_routes import router as client_router
from app.api.asset_routes import router as asset_router
from app.api.portfolio_routes import router as portfolio_router

app = FastAPI(title="Finance Portfolio API")

app.include_router(client_router)
app.include_router(asset_router)
app.include_router(portfolio_router)
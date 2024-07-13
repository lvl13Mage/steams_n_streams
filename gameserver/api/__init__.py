from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from api.routes.debug import router as debug_router

app = FastAPI()

api_router = APIRouter()
api_router.include_router(debug_router)
@app.get("/")
def health_check():
    return {"status": "ok"}

app.include_router(api_router)
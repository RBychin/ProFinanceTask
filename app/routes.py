from fastapi import APIRouter

from app.views import app

router = APIRouter()

router.include_router(app)

import fastapi
from fastapi import HTTPException

from src.accounting.routes import router as accounting_router

router = fastapi.APIRouter()
router.include_router(accounting_router, prefix="/accounting")


@router.get("/health-check")
def health_check():
    return HTTPException(status_code=200, detail={"health_check": True})

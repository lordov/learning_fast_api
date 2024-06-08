import time
from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.operations.models import Operation
from src.operations.schemas import OperationCreate


router = APIRouter(
    prefix="/operations",
    tags=["Operations"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def get_specific_operations(
    operation_type: str,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        query = select(Operation).where(Operation.type == operation_type)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.scalars().all(),
            "details": None
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("")
async def add_specific_operations(
    new_operation: OperationCreate,
    sessoin: AsyncSession = Depends(get_async_session)
):
    stmt = insert(Operation).values(new_operation.model_dump())
    await sessoin.execute(stmt)
    await sessoin.commit()
    return {"status": "ok"}


@router.get("/long_operation")
@cache(expire=30)
def get_long_operation():
    time.sleep(2)
    return "Много много данных, сто лет"

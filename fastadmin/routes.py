from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from starlette.requests import Request
from starlette.responses import JSONResponse
from tortoise import Model

from fastadmin.depends import get_model, get_query
from fastadmin.schemas import Query

router = APIRouter()


@router.get("/{resource}")
async def get(
    resource: str,
    model: Model = Depends(get_model),
    query: Query = Depends(get_query),
):
    count = await model.all().count()
    data = (
        await model.filter(**query.filter)
        .order_by(query.sort)
        .limit(query.limit)
        .offset(query.offset)
        .values()
    )
    return JSONResponse(
        content=jsonable_encoder(data),
        headers={
            "Content-Range": f"{resource} {query.offset}-{query.offset + query.limit}/{count}"
        },
    )


@router.get("/{resource}/{pk}")
async def get_one(
    pk: int,
    model: Model = Depends(get_model),
):
    obj = await model.get(pk=pk)
    return obj


@router.post("/{resource}")
async def create(
    request: Request,
    model: Model = Depends(get_model),
):
    body = await request.json()
    obj = await model.create(**body)
    return obj


@router.put("/{resource}/{pk}")
async def update(
    request: Request,
    pk: int,
    model: Model = Depends(get_model),
):
    body = await request.json()
    obj = await model.get(pk=pk)
    await obj.update_from_dict(body).save()
    return obj


@router.delete("/{resource}/{pk}")
async def delete(
    pk: int,
    model: Model = Depends(get_model),
):
    obj = await model.get(pk=pk)
    await obj.delete()
    return obj

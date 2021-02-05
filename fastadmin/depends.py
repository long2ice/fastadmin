import json
from typing import Optional

from fastapi.params import Path, Query
from tortoise import Tortoise

from fastadmin.schemas import Query as Qy
from fastadmin.types import Order


def get_model(resource: str = Path(...)):
    for app, models in Tortoise.apps.items():
        model = models.get(resource.title())
        if model:
            return model


async def get_query(
    filter_: Optional[str] = Query(None, alias="filter"),
    range_: Optional[str] = Query(None, alias="range"),
    sort: Optional[str] = None,
):
    query = Qy()
    if filter_:
        query.filter = json.loads(filter_)
    if range_:
        range_ = json.loads(range_)
        query.offset = range_[0]
        query.limit = range_[1] - range_[0]
    if sort:
        sort = json.loads(sort)
        field = sort[0]
        order = sort[1]
        if order == Order.DESC:
            field = f"-{field}"
        query.sort = field
    return query

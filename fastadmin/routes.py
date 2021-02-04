from typing import Optional

from fastapi import APIRouter
from starlette.responses import JSONResponse

from fastadmin.types import Order

router = APIRouter()


@router.get("/{resource}")
async def get(
    resource: str,
    _start: Optional[int],
    _end: Optional[int],
    _order: Optional[Order],
    _sort: Optional[str],
):
    return JSONResponse(
        content=[
            {
                "id": 1,
                "name": "Leanne Graham",
                "username": "Bret",
                "email": "Sincere@april.biz",
                "address": {
                    "street": "Kulas Light",
                    "suite": "Apt. 556",
                    "city": "Gwenborough",
                    "zipcode": "92998-3874",
                    "geo": {"lat": "-37.3159", "lng": "81.1496"},
                },
                "phone": "1-770-736-8031 x56442",
                "website": "hildegard.org",
                "company": {
                    "name": "Romaguera-Crona",
                    "catchPhrase": "Multi-layered client-server neural-net",
                    "bs": "harness real-time e-markets",
                },
            }
        ],
        headers={"X-Total-Count": "1"},
    )


@router.get("/{resource}/{pk}")
async def get_one(resource: str, pk: int):
    print(resource, pk)


@router.post("/{resource}")
async def create(
    resource: str,
):
    print(resource)


@router.put("/{resource}/{pk}")
async def update(resource: str, pk: int):
    print(resource, pk)


@router.delete("/{resource}/{pk}")
async def delete(resource: str, pk: int):
    print(resource, pk)

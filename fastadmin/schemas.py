from typing import Optional

from pydantic import BaseModel


class Query(BaseModel):
    filter: Optional[dict]
    limit: Optional[int]
    offset: Optional[int]
    sort: Optional[str]

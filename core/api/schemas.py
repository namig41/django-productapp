from typing import (
    Any,
    Generic,
    TypeVar,
)

from pydantic import (
    BaseModel,
    Field,
)

from core.api.filters import PaginationOut


TData = TypeVar("TData")
TListItem = TypeVar("TListItem")


class PingResponseSchema(BaseModel):
    result: bool


class ListPaginatedResponse(BaseModel, Generic[TListItem]):
    items: list[TListItem]
    pagination: PaginationOut


class ApiResponse(BaseModel, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    errors: list[Any] = Field(default_factory=list)

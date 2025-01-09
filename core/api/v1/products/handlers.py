from django.http import HttpRequest
from ninja import (
    Query,
    Router,
)

from punq import Container

from core.api.filters import PaginationIn
from core.api.schemas import (
    ApiResponse,
    ListPaginatedResponse,
    PaginationOut,
)
from core.api.v1.products.filters import ProductFilters
from core.api.v1.products.schemas import ProductSchema
from core.apps.products.filters.products import ProductsFilters as ProductFiltersEntity
from core.apps.products.services.products import BaseProductService
from project.containers import get_container


router = Router(tags=["Products"])


@router.get("", response=ApiResponse[ListPaginatedResponse[ProductSchema]])
def get_product_list_handler(
    request: HttpRequest,
    filters: Query[ProductFilters],
    pagination_in: Query[PaginationIn],
) -> ApiResponse[ListPaginatedResponse[ProductSchema]]:
    container: Container = get_container()
    service: BaseProductService = container.resolve(BaseProductService)
    product_list = service.get_product_list(
        filters=ProductFiltersEntity(search=filters.search),
        pagination=pagination_in,
    )
    product_count = service.get_product_count(filters=filters)
    items = [ProductSchema.from_entity(obj) for obj in product_list]
    pagination_out = PaginationOut(
        offset=0,
        limit=product_count,
        total=product_count,
    )
    return ApiResponse(
        data=ListPaginatedResponse(items=items, pagination=pagination_out),
    )

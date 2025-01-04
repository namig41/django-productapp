from django.http import HttpRequest
from ninja import Router

from core.api.schemas import ApiResponse, ListPaginatedResponse, PaginationOut
from core.api.v1.products.schemas import ProductSchema
from core.apps.products.services.products import BaseProductService, ORMProductService

router = Router(tags=["Products"])


@router.get("", response=ApiResponse[ListPaginatedResponse[ProductSchema]])
def get_product_list_handler(
    request: HttpRequest,
) -> ApiResponse[ListPaginatedResponse[ProductSchema]]:
    service: BaseProductService = ORMProductService()
    product_list = service.get_product_list()
    product_count = service.get_product_count()
    items = [ProductSchema.from_entity(obj) for obj in product_list]
    pagination = PaginationOut(
        offset=0,
        limit=product_count,
        total=product_count,
    )
    return ApiResponse(data=ListPaginatedResponse(items=items, pagination=pagination))

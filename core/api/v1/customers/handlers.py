from django.http import HttpResponse
from ninja import Router
from ninja.errors import HttpError

from punq import Container

from core.api.schemas import ApiResponse
from core.api.v1.customers.schemas import (
    AuthInSchema,
    AuthOutSchema,
    TokenInSchema,
    TokenOutSchema,
)
from core.app.common.exceptions import ServiceException
from core.app.customers.services.auth import BaseAuthService
from core.project.containers import get_container


router = Router(tags=["Customers"])


@router.post("auth", response=ApiResponse[AuthOutSchema], operation_id="authorize")
def auth_handler(
    request: HttpResponse,
    schema: AuthInSchema,
) -> ApiResponse[AuthOutSchema]:
    conainter: Container = get_container()
    service: BaseAuthService = conainter.resolve(BaseAuthService)

    service.authorize(schema.phone)
    return ApiResponse(
        data=AuthOutSchema(
            message=f"Код отправлен на: {schema.phone}",
        ),
    )


@router.post("confirm", response=ApiResponse[TokenOutSchema], operation_id="confirm")
def get_token_handler(
    request: HttpResponse,
    schema: TokenInSchema,
) -> ApiResponse[TokenOutSchema]:
    conainter: Container = get_container()
    service: BaseAuthService = conainter.resolve(BaseAuthService)

    try:
        token = service.confirm(schema.code, schema.phone)
    except ServiceException as exception:
        raise HttpError(
            status_code=400,
            message=exception.message,
        )

    return ApiResponse(
        data=TokenOutSchema(
            token=token,
        ),
    )

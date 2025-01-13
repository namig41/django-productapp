import pytest

from core.app.products.services.products import (
    BaseProductService,
    ORMProductService,
)


@pytest.fixture(scope="session")
def product_service() -> BaseProductService:
    return ORMProductService()

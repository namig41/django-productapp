import pytest
from core.apps.products.services.products import BaseProductService, ORMProductService

@pytest.fixture(scope="session")
def product_service() -> BaseProductService:
    return ORMProductService()
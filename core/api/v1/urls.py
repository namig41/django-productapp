from ninja import Router

from core.api.v1.customers.handlers import router as customers_router
from core.api.v1.products.handlers import router as product_router
from core.api.v1.reviews.handlers import router as reviews_router


router = Router(tags=["v1"])
router.add_router("reviews/", reviews_router)
router.add_router("products/", product_router)
router.add_router("customers/", customers_router)

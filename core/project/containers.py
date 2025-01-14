from functools import lru_cache

from punq import Container

from core.app.customers.services.auth import (
    AuthService,
    BaseAuthService,
)
from core.app.customers.services.codes import (
    BaseCodeService,
    DjangoCacheCodeService,
)
from core.app.customers.services.customers import (
    BaseCustomerService,
    ORMCustomerService,
)
from core.app.customers.services.senders import (
    BaseSenderService,
    DummySenderService,
)
from core.app.products.services.products import (
    BaseProductService,
    ORMProductService,
)
from core.app.products.services.reviews import (
    BaseReviewService,
    BaseReviewValidatorService,
    ComposedReviewRatingValidatorService,
    ORMReviewService,
    ReviewRatingValidatorService,
    SingleReviewValidatorService,
)
from core.app.products.use_cases.reviews.create import CreateReviewUseCase


@lru_cache(1)
def get_container():
    return _initialize_container()


def _initialize_container() -> Container:
    container: Container = Container()

    container.register(BaseProductService, ORMProductService)

    container.register(BaseCustomerService, ORMCustomerService)
    container.register(BaseCodeService, DjangoCacheCodeService)
    container.register(BaseSenderService, DummySenderService)
    container.register(BaseAuthService, AuthService)

    container.register(BaseReviewService, ORMReviewService)
    container.register(ReviewRatingValidatorService)
    container.register(SingleReviewValidatorService)

    def build_validators() -> BaseReviewValidatorService:
        return ComposedReviewRatingValidatorService(
            validators=[
                container.resolve(ReviewRatingValidatorService),
                container.resolve(SingleReviewValidatorService),
            ],
        )

    container.register(BaseReviewValidatorService, factory=build_validators)
    container.register(CreateReviewUseCase)

    return container

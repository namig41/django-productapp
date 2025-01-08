from functools import lru_cache

from punq import Container

from core.apps.customers.services.auth import (
    AuthService,
    BaseAuthService,
)
from core.apps.customers.services.codes import (
    BaseCodeService,
    DjangoCacheCodeService,
)
from core.apps.customers.services.customers import (
    BaseCustomerService,
    ORMCustomerService,
)
from core.apps.customers.services.senders import (
    BaseSenderService,
    DummySenderService,
)
from core.apps.products.services.products import (
    BaseProductService,
    ORMProductService,
)


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

    return container

from abc import (
    ABC,
    abstractmethod,
)

from core.apps.products.entities.reviews import Review as ReviewEntity


class BaseReviewService(ABC):
    @abstractmethod
    def create_review(
        self,
        product_id: int,
        customer_token: str,
        rating: str,
        text: str,
    ) -> ReviewEntity: ...

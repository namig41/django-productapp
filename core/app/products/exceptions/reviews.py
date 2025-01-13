from dataclasses import dataclass

from core.app.common.exceptions import ServiceException


@dataclass(eq=False)
class ReviewInvalidRating(ServiceException):
    rating: int

    @property
    def message(self) -> str:
        return "Rating is not valid"

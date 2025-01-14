from dataclasses import dataclass

from core.app.common.exceptions import ServiceException


@dataclass(eq=False)
class ReviewInvalidRating(ServiceException):
    rating: int

    @property
    def message(self) -> str:
        return "Rating is not valid"


@dataclass(eq=False)
class SingleReviewError(ServiceException):

    @property
    def message(self) -> str:
        return "The review already exsists"

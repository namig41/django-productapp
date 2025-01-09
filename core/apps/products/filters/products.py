from dataclasses import dataclass


@dataclass(frozen=True)
class ProductsFilters:
    search: str | None = None

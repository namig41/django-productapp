from uuid import uuid4

from django.db import models

from core.apps.common.models import TimeBaseModel
from core.apps.customers.entities import CustomerEntity


class Customer(TimeBaseModel):
    phone = models.CharField(
        verbose_name="Phone Number",
        max_length=20,
        unique=True,
    )

    token = models.CharField(
        verbose_name="User token",
        max_length=255,
        unique=True,
        default=uuid4,
    )

    def __str__(self) -> str:
        return self.phone

    def to_entity(self) -> CustomerEntity:
        return CustomerEntity(
            phone=self.phone,
            created_at=self.created_at,
        )

    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиенты"

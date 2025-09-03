"""Brightsites API models."""

from datetime import datetime

from pydantic import BaseModel as PydanticBaseModel
from pydantic import EmailStr, Field


class _BaseModel(PydanticBaseModel, strict=True):
    """Base model for all Brightsites models."""


class PaginationMeta(_BaseModel):
    """Pagination metadata."""

    total: int
    offset: int
    limit: int


class PaginatedResponse(_BaseModel):
    """A paginated response."""

    meta: PaginationMeta


class Order(_BaseModel):
    """An order."""

    created_at: datetime = Field(strict=False)
    updated_at: datetime = Field(strict=False)
    order_id: int
    shipping_method: str
    tracking: str
    status: str
    customer: EmailStr


class OrdersList(PaginatedResponse):
    """A list of orders."""

    orders: list[Order]

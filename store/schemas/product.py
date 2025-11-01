from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field
from store.models.base import CreateBaseModel


class ProductBase(BaseModel):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status (active/inactive)")


class ProductIn(ProductBase):
    pass


class ProductOut(ProductIn, CreateBaseModel):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Product name")
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[Decimal] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")
    updated_at: Optional[datetime] = Field(None, description="Timestamp of last update")


class ProductUpdateOut(ProductOut):
    pass

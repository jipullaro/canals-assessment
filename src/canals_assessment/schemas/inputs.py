from enum import Enum

from pydantic import BaseModel, EmailStr


class ProductsEnum(str, Enum):
    BOOK = "book"
    LAPTOP = "laptop"
    SMARTWATCH = "smartwatch"
    WIRELESS_EARBUDS = "wireless_earbuds"


class ItemInput(BaseModel):
    product: ProductsEnum
    quantity: int


class CustomerInput(BaseModel):
    name: str
    email: EmailStr


class OrderInput(BaseModel):
    customer: CustomerInput
    shipping_address: str
    product_list: list[ItemInput]

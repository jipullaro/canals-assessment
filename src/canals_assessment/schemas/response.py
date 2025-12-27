from pydantic import BaseModel


class OrderResponse(BaseModel):
    order_id: str
    status: str

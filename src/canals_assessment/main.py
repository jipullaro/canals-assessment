from fastapi import FastAPI

from canals_assessment.schemas.inputs import OrderInput
from canals_assessment.schemas.response import OrderResponse

app = FastAPI()


@app.post("/orders")
def read_item(order_input: OrderInput):
    return OrderResponse(order_id="12345", status="created")


@app.get("/orders/{order_id}")
def read_order(order_id: str):
    return OrderResponse(order_id="12345", status="created")

from ninja import Schema


class CartSchemaIn(Schema):
    product_id: int
    quantity: int
    observation: str
    is_order: bool
    is_request: bool
    pickup_datetime: str

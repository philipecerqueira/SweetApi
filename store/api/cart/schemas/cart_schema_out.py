from ninja import Schema


class CartSchemaOut(Schema):
    id: int
    product_id: int
    quantity: int
    observation: str

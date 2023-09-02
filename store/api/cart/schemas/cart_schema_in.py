from ninja import Schema


class CartSchemaIn(Schema):
    product_id: int
    quantity: int
    observation: str

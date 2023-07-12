from ninja import Schema


class ProductSchemaIn(Schema):
    name: str
    category_id: int
    quantity: int
    price_sell: float
    price_buy: float

from ninja import Schema


class ProductSchemaOut(Schema):
    id: int
    name: str
    category_id: int
    price_sell: float
    price_buy: float
    is_order: bool
    is_request: bool
    active: bool

from typing import List

from django.shortcuts import get_list_or_404
from ninja import Schema

from ...models import Product
from .product_router import product_router


class ProductSchemaOut(Schema):
    id: int
    name: str
    category_id: int
    quantity: int
    price_sell: float
    price_buy: float


@product_router.get('/product', response=List[ProductSchemaOut])
def get_products(request):
    product = get_list_or_404(Product)
    return product
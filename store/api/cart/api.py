from typing import List

from django.shortcuts import get_list_or_404
from ninja import Router, Schema

from ...models import Cart, Product
from .schemas.cart_schema_in import CartSchemaIn
from .schemas.cart_schema_out import CartSchemaOut

cart_router = Router()


@cart_router.get('/', response={200: List[CartSchemaOut], 404: object})
def get_cart(request):
    cart = get_list_or_404(Cart)
    return cart


@cart_router.post("/", response={200: None, 401: str})
def add_cart(request, payload: CartSchemaIn):
    print("PAYLOAD", payload)
    product_id = payload.product_id

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return 401, f"O produto com o ID {product_id} não existe."

    Cart.objects.create(**payload.dict())
    return 200, None


@cart_router.put('/{int:id}', response={200: None})
def update_cart(request, id: int, payload: CartSchemaIn):
    cart = get_object_or_404(Cart, id=id)
    for attr, value in payload.dict().items():
        setattr(cart, attr, value)
    cart.save()
    return 200, None


@cart_router.delete('/{int:id}', response={200: None})
def delete_cart(request, id: int):
    cart = get_object_or_404(Cart, id=id)
    cart.delete()
    return 200, None

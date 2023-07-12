from typing import List

from django.shortcuts import get_list_or_404
from ninja import Router, Schema

from ...models import Product
from .schemas.product_schema_in import ProductSchemaIn
from .schemas.product_schema_out import ProductSchemaOut

product_router = Router()


@product_router.get('/', response=List[ProductSchemaOut])
def get_products(request):
    product = get_list_or_404(Product)
    return product


@product_router.get('/{int:id}', response=ProductSchemaOut)
def get_product_by_id(request, id: int):
    product = get_object_or_404(Product, id=id)
    return product


@product_router.post("/", response={200: None})
def create_product(request, payload: ProductSchemaIn):
    Product.objects.create(**payload.dict())
    return 200, None


@product_router.put('/{int:id}', response={200: None})
def update_product(request, id: int, payload: ProductSchemaIn):
    product = get_object_or_404(Product, id=id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return 200, None


@product_router.delete('/{int:id}', response={200: None})
def delete_product(request, id: int):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return 200, None

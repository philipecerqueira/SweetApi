from typing import List

from django.shortcuts import get_list_or_404
from ninja import Router, Schema

from ...models import Category, Product
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


@product_router.post("/", response={200: None, 401: str})
def create_product(request, payload: ProductSchemaIn):
    category_id = payload.category_id

    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return 401, f"O produto com o ID {category_id} não existe."

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

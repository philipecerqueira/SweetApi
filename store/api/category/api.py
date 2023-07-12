from typing import List

from django.shortcuts import get_list_or_404
from ninja import Router, Schema

from ...models import Category
from .schemas.category_schema_in import CategorySchemaIn
from .schemas.category_schema_out import CategorySchemaOut

category_router = Router()


@category_router.get('/', response=List[CategorySchemaOut])
def get_categorys(request):
    category = get_list_or_404(Category)
    return category


@category_router.get('/{int:id}')
def get_category_by_id(request, id: int):
    category = get_object_or_404(Category, id=id)
    return model_to_dict(category)


@category_router.post("/", response={200: None})
def create_category(request, payload: CategorySchemaIn):
    Category.objects.create(**payload.dict())
    return 200, None


@category_router.put('/{int:id}', response={200: None})
def update_category(request, id: int, payload: CategorySchemaIn):
    category = get_object_or_404(Category, id=id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return 200, None


@category_router.delete('/{int:id}', response={200: None})
def delete_category(request, id: int):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return 200, None

from typing import List

from django.forms.models import model_to_dict
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router, Schema

from .models import Category, Image, Product

router = Router()

class CategorySchemaOut(Schema):
    id: int
    title: str

class CategorySchemaIn(Schema):
    title: str

@router.get('/category', response=List[CategorySchemaOut])
def get_categorys(request):
    category = get_list_or_404(Category)
    return category


@router.get('/category/{int:id}')
def get_category_by_id(request, id: int):
    category = get_object_or_404(Category, id=id)
    return model_to_dict(category)


@router.post("/category", response={200: None})
def create_category(request, payload: CategorySchemaIn):
    Category.objects.create(**payload.dict())
    return 200, None


@router.put('/category/{int:id}', response={200: None})
def update_category(request, id: int, payload: CategorySchemaIn):
    category = get_object_or_404(Category, id=id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return 200, None


@router.delete('/category/{int:id}', response={200: None})
def delete_category(request, id: int):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return 200, None
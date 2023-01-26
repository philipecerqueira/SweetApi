from typing import List

from django.shortcuts import get_list_or_404

from ...models import Category
from .category_router import category_router
from .category_schema_out import CategorySchemaOut


@category_router.get('/', response=List[CategorySchemaOut])
def get_categorys(request):
    category = get_list_or_404(Category)
    return category
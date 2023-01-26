from ninja import Router

from .category.category_router import category_router
from .product.product_router import product_router

store_router = Router()


store_router.add_router('/category', category_router)
store_router.add_router('/product', product_router)
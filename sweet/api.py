from ninja import NinjaAPI

from store.api import router as store_router

api = NinjaAPI()

api.add_router('/store/', store_router)
from ninja import NinjaAPI

from store.api.store_router import store_router

# from store.apiOld import router as store_router


api = NinjaAPI()

api.add_router('/store', store_router)

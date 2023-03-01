from fastapi.routing import APIRouter

from server.web.api import users, deals

api_router = APIRouter()
api_router.include_router(users.views.router, prefix="/users", tags=["users"])
api_router.include_router(deals.views.router, prefix="/deals", tags=["deals"])

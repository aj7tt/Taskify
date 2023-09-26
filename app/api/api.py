from fastapi import APIRouter


router = APIRouter()


# route for user api service
from .controllers.user_controller import user as userAPIRouter
router.include_router(userAPIRouter)

 
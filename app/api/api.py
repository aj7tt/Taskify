from fastapi import APIRouter


router = APIRouter()


# route for user api service
from .controllers.user_controller import user as userAPIRouter
router.include_router(userAPIRouter)

# route for task api service
from .controllers.task_controller import task as taskAPIRouter
router.include_router(taskAPIRouter)
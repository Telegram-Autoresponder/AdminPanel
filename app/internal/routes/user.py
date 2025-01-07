from fastapi import APIRouter, Depends
from app.pkg import models
from dependency_injector.wiring import Provide, inject
from app.internal.services.user import UserService
from app.internal.services import Services

router = APIRouter(
	prefix="/user"
)

@router.post(
	"",
)
@inject
async def create_user(
	cmd: models.app.user_schema.CreateUser,
	user_service: UserService = Depends(Provide[Services.user_service])
):
	await user_service.create(cmd=cmd)

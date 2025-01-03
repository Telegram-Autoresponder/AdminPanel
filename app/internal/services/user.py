from app.internal.repository.postgresql.user import UserRepository
from app.pkg import models

__all__ = [
	"UserService",
]

class UserService:
	__user_repository: UserRepository

	def __init__(
		self,
		user_repository: UserRepository,
	):
		self.__user_repository = user_repository

	async def create(self, cmd: models.app.user_schema.CreateUser):
		await self.__user_repository.create_user(cmd=cmd)

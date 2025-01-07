from app.internal.repository.repository import Repository
from app.pkg import models
from app.internal.repository.postgresql.connection import get_connection


class UserRepository(Repository):

	async def create_user(self, cmd: models.app.user_schema.CreateUser):
		async with get_connection() as connection:
			connection.add(models.app.user_sql.User(**cmd.to_dict()))
			await connection.commit()


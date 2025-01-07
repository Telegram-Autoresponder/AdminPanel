from app.pkg.models.base import BaseModel

__all__ = [
	"CreateUser",
]


class BaseUser(BaseModel):
	"""Base user model."""


class CreateUser(BaseUser):
	telegram_name: str
	telegram_token: str
	real_name: str

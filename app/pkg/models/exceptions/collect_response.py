from app.pkg.models.base import BaseAPIException
from fastapi import status

__all__ = [
	"EmptyResult"
]

class EmptyResult(BaseAPIException):
	"""Empty result."""
	message = "Empty result"
	status_code = status.HTTP_404_NOT_FOUND



from app.pkg.models.app.sqlalchemy import Base
import sqlalchemy


class User(Base):
	__tablename__ = "users"

	id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True, index=True)
	telegram_name = sqlalchemy.Column(sqlalchemy.String(60), unique=True)
	telegram_token = sqlalchemy.Column(sqlalchemy.String(255), unique=True)
	real_name = sqlalchemy.Column(sqlalchemy.String(255))
	active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

"""Service layer."""

from dependency_injector import containers, providers

from app.internal.repository import Repositories, postgresql

from app.internal.services.user import UserService

class Services(containers.DeclarativeContainer):
    """Containers with services."""

    repositories: postgresql.Repositories = providers.Container(
        Repositories.postgres,
    )

    user_service: UserService = providers.Factory(
        UserService,
        user_repository=repositories.user_repository
    )

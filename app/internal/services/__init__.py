"""Service layer."""

from dependency_injector import containers, providers

from app.internal.repository import Repositories, postgresql
from app.internal.services.city import CityService


class Services(containers.DeclarativeContainer):
    """Containers with services."""


    repositories: postgresql.Repositories = providers.Container(
        Repositories.postgres,
    )
    city_service = providers.Factory(
        CityService,
        city_repository=repositories.city_repository,
    )


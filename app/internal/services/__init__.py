"""Service layer."""

from dependency_injector import containers, providers

from app.internal.repository import Repositories, postgresql


class Services(containers.DeclarativeContainer):
    """Containers with services."""


    repositories: postgresql.Repositories = providers.Container(
        Repositories.postgres,
    )


from typing import TypeVar

from src.database.entity import Entity

EntityT = TypeVar("EntityT", bound=Entity)


class Repository:
    def __init__(self, database_context) -> None:
        self._database_context = database_context

    async def _query():
        pass

    async def _count():
        pass

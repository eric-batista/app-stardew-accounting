import re
from typing import TypeVar

from sqlalchemy import MetaData, inspect
from sqlalchemy.orm import as_declarative, declared_attr
from sqlalchemy.orm.properties import ColumnProperty


def _to_snake(string: str):
    initial, *rest = string
    rest = "".join(rest)
    parsed = re.sub(
        "([a-z])([A-Z])",
        lambda match: "_".join(item.lower() for item in match.groups()),
        rest,
    )
    return f"{initial.lower()}{parsed}"


T = TypeVar("T")


def _as_declarative(cls: type[T]) -> type[T]:
    return as_declarative()(cls)


@_as_declarative
class Entity:
    __name__: str
    metadata: MetaData

    def __init__(self, **kwargs):
        ...

    @declared_attr
    def __tablename__(cls):
        return _to_snake(cls.__name__.removesuffix("Entity"))

    def _fields(self):
        for prop in inspect(type(self)).iterate_properties:
            if isinstance(prop, ColumnProperty):
                yield prop.key

    def dict(self):
        return {key: getattr(self, key) for key in self._fields()}

    def set(self, **vals):
        for key, val in vals.items():
            setattr(self, key, val)

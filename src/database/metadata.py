from src.core.settings import ROOT
from src.database.autodiscovery import ClassFinder
from src.database.entity import Entity


def get_metadata():
    ClassFinder(Entity, ROOT).find()
    return Entity.metadata

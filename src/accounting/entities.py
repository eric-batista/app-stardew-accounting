from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.accounting.enum import ArtisanGoodsTypeEnum, CropGrowTypeEnum, CropTypeEnum
from src.database.entity import Entity


class Crops(Entity):
    id = sa.Column(sa.Text(), primary_key=True, index=True)
    name = sa.Column(sa.Text(), index=True)
    description = sa.Column(sa.Text())
    buy_value = sa.Column(sa.Integer(), nullable=False)
    type = sa.Column(sa.Enum(CropGrowTypeEnum), nullable=False)
    days_to_harvest = sa.Column(sa.Integer(), nullable=False)
    days_before_first_harvest = sa.Column(sa.Integer())
    season_id = sa.Column(sa.Text(), sa.ForeignKey("seasons.id"))
    season = relationship("Seasons", lazy="selection", back_populates="crops")


class Animals(Entity):
    id = sa.Column(sa.Text(), primary_key=True, index=True)
    name = sa.Column(sa.Text(), index=True)
    description = sa.Column(sa.Text())
    buy_value = sa.Column(sa.Integer())
    days_to_produce = sa.Column(sa.Integer())
    affinity_hearts = sa.Column(sa.Integer())


class Products(Entity):
    id = sa.Column(sa.Text(), primary_key=True, index=True)
    name = sa.Column(sa.Text(), index=True)
    description = sa.Column(sa.Text())
    animal_id = sa.Column(sa.Text(), sa.ForeignKey("animals.id"))
    animal = relationship("Animals")


class CropsRank(Entity):
    id = sa.Column(sa.Text(), primary_key=True, index=True)
    name = sa.Column(sa.Text(), index=True)
    description = sa.Column(sa.Text())
    type = sa.Column(sa.Enum(CropTypeEnum))
    value = sa.Column(sa.Integer())
    crop_id = sa.Column(sa.Text(), sa.ForeignKey("crops.id"))
    crops = relationship("Crops", lazy="selectin")


class Seasons(Entity):
    id = sa.Column(sa.Text(), primary_key=True, index=True)
    name = sa.Column(sa.Text(), index=True)
    description = sa.Column(sa.Text())
    crops = relationship("Crops", back_populates="season")


class ArtisanGoods(Entity):
    id = sa.Column(sa.Text(), primary_key=True, index=True)
    name = sa.Column(sa.Text(), index=True)
    description = sa.Column(sa.Text())
    type = sa.Column(sa.Enum(ArtisanGoodsTypeEnum), nullable=False)
    value = sa.Column(sa.Integer(), nullable=False)
    crop_id = sa.Column(sa.Text(), sa.ForeignKey("crops.id"))
    product_id = sa.Column(sa.Text(), sa.ForeignKey("products.id"))

from pydantic import BaseModel
from src.accounting.enum import CropTypeEnum, CropGrowTypeEnum, ArtisanGoodsTypeEnum, ProductTypeEnum
from typing import List


class Model(BaseModel):
    id: str
    name: str
    description: str


class ArtisanGoodsModel(Model):
    type: ArtisanGoodsTypeEnum
    value: int


class CropRankModel(Model):
    type: CropTypeEnum
    value: int


class CropModel(Model):
    crop_rank: CropRankModel
    buy_value: int
    type: CropGrowTypeEnum
    days_to_harvest: int
    days_before_first_harvest: int | None = None
    artisan_good: ArtisanGoodsModel


class SeasonModel(Model):
    crops: List[CropModel]


class ProductModel(Model):
    value: int
    type: ProductTypeEnum
    ArtisanGoods: ArtisanGoodsModel


class AnimalModel(Model):
    affinity_hearts: int
    buy_value: int
    days_to_produce: int
    product: ProductModel

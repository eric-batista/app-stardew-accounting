import enum


class RankTypeEnum(enum.Enum):
    DEFAULT: enum.auto()
    SILVER: enum.auto()
    GOLD: enum.auto()
    IRIDIUM: enum.auto()


class CropTypeEnum(RankTypeEnum):
    ...


class ArtisanGoodsTypeEnum(RankTypeEnum):
    ...


class ProductTypeEnum(RankTypeEnum):
    ...


class CropGrowTypeEnum(enum.Enum):
    SINGLE_HARVEST: enum.auto()
    MULTI_HARVEST: enum.auto()

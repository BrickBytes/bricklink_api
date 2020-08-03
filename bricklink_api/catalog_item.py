import enum as _enum

from . import helper as _helper
from .method import method as _method, Method


class Type(_enum.Enum):
  MINIFIG = "Minifig"
  PART = "Part"
  SET = "Set"
  BOOK = "Book"
  GEAR = "Gear"
  CATALOG = "Catalog"
  INSTRUCTION = "Instruction"
  UNSORTED_LOT = "Unsorted Lot"
  ORIGINAL_BOX = "Original Box"


class GuideType(_enum.Enum):
  SOLD = "sold"
  STOCK = "stock"
  DEFAULT = "stock"


class NewOrUsed(_enum.Enum):
  NEW = "N"
  USED = "U"

class VATSetting(_enum.Enum):
  N = "N"
  Y = "Y"
  O = "O"
  EXCLUDE = "N"
  INCLUDE = "Y"
  INCLUDE_AS_NORWAY = "O"
  DEFAULT = "N"


def get_item(
    type_: Type,
    no: str,
    **kwargs
) -> dict:
  return _method(Method.GET, f'/items/{_helper.deenumize(type_)}/{no}',**kwargs)


def get_item_image(
    type_: Type,
    no: str,
    color_id: int,
    **kwargs
) -> dict:
  return _method(
      Method.GET,
      f'/items/{_helper.deenumize(type_)}/{no}/images/{color_id}',
      **kwargs
  )


def get_supersets(
    type_: Type,
    no: str,
    color_id: int = None,
    **kwargs
) -> dict:
  params = _helper.norm_params({
      "color_id": color_id,
  })
  return _method(Method.GET, f'/items/{_helper.deenumize(type_)}/{no}/supersets',
      params=params,
      **kwargs
  )


def get_subsets(
    type_: Type,
    no: str,
    color_id: int = None,
    box: bool = None,
    instruction: bool = None,
    break_minifigs: bool = None,
    break_subsets: bool = None,
    **kwargs
) -> dict:
  params = _helper.norm_params({
      "color_id": color_id,
      "box": box,
      "instruction": instruction,
      "break_minifigs": break_minifigs,
      "break_subsets": break_subsets,
  })
  return _method(Method.GET, f'/items/{_helper.deenumize(type_)}/{no}/subsets',
      params=params,
      **kwargs
  )


def get_price_guide(
    type_: Type,
    no: str,
    color_id: int = None,
    guide_type: GuideType = None,
    new_or_used: NewOrUsed = None,
    country_code: str = None,
    region: str = None,
    currency_code: str = None,
    vat: VATSetting = None,
    **kwargs
) -> dict:
  params = _helper.norm_params({
      "color_id": color_id,
      "guide_type": guide_type,
      "new_or_used": new_or_used,
      "country_code": country_code,
      "region": region,
      "currency_code": currency_code,
      "vat": vat,
  })
  return _method(Method.GET, f'/items/{_helper.deenumize(type_)}/{no}/price',
      params=params,
      **kwargs
  )


def get_known_colors(
    type_: Type,
    no: str,
    **kwargs
) -> dict:
  return _method(Method.GET, f'/items/{_helper.deenumize(type_)}/{no}/colors',**kwargs)

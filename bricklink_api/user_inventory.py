import enum as _enum

from . import helper as _helper
from .method import method as _method

from . import catalog_item as _catalog_item


class Status(_enum.Enum):
  Y = "available"
  S = "in stockroom A"
  B = "in stockroom B"
  C = "in stockroom C"
  N = "unavailable"
  R = "reserved"


def get_inventories(
    item_type: _catalog_item.Type = None,
    status: str = None,  #TODO!
    category_id: str = None,  #TODO!
    color_id: str = None, #TODO!
    **kwargs
) -> dict:
  params = _helper.norm_params({
    "item_type": item_type,
    "status": status,
    "category_id": category_id,
    "color_id": color_id,
  })
  return _method("GET", "/inventories",
      params = params,
      **kwargs
  )


def get_inventory(
    inventory_id: int,
    **kwargs
) -> dict:
  return _method("GET", f'/inventories/{inventory_id}',
      **kwargs
  )


def create_inventory(
    inventory_resource: dict,
    **kwargs
) -> dict:
  return _method("POST", "/inventories",
      json = inventory_resource,
      **kwargs
  )


def create_inventories(
    inventory_resources: list,
    **kwargs
) -> dict:
  return _method("POST", "/inventories",
      json = inventory_resources,
      **kwargs
  )


def update_inventory(
    inventory_id: int,
    inventory_resource: dict,
    **kwargs
) -> dict:
  return _method("PUT", f'/inventories/{inventory_id}',
      json = inventory_resource,
      **kwargs
  )


def delete_inventory(
    inventory_id: int,
    **kwargs
) -> dict:
  return _method("DELETE", f'/inventories/{inventory_id}',
      **kwargs
  )

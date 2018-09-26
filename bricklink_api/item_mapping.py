from .method import method as _method

from . import catalog_item as _catalog_item


def get_element_id(
    type_: _catalog_item.Type,
    no: str,
    **kwargs
) -> dict:
  return _method("GET", f'/item_mapping/{type_}/{no}',
      **kwargs
  )


def get_item_number(
    element_id: int,
    **kwargs
) -> dict:
  return _method("GET", f'/item_mapping/{element_id}',
      **kwargs
  )

from . import catalog_item as _catalog_item
from . import method as _method


def get_element_id(
    type_: _catalog_item.Type,
    no: str,
    **kwargs
) -> dict:
  return _method.method(
      _method.Method.GET,
      f'/item_mapping/{type_}/{no}',
      **kwargs
  )


def get_item_number(
    element_id: int,
    **kwargs
) -> dict:
  return _method.method(
      _method.Method.GET,
      f'/item_mapping/{element_id}',
      **kwargs
  )

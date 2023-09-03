from . import method as _method


def get_shipping_method_list(**kwargs) -> dict:
  return _method.method(
      _method.Method.GET,
      "/settings/shipping_methods",
      **kwargs
  )


def get_shipping_method(
    method_id: int,
    **kwargs
) -> dict:
  return _method.method(
      _method.Method.GET,
      f'/settings/shipping_methods/{method_id}',
      **kwargs
  )

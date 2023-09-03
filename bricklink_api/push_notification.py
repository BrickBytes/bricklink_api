from . import method as _method


def get_notifications(**kwargs) -> dict:
  return _method.method(
      _method.Method.GET,
      "/notifications",
      **kwargs
  )

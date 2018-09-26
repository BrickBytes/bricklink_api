from .method import method as _method


def get_notifications(**kwargs) -> dict:
  return _method("GET", "/notifications",
      **kwargs
  )

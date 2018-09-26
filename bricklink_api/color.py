from .method import method as _method


def get_color_list(**kwargs) -> dict:
  return _method("GET", "/colors",
      **kwargs
  )


def get_color(
    color_id: int,
    **kwargs
) -> dict:
  return _method("GET", f'/colors/{color_id}',
      **kwargs
  )

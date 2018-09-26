from .method import method as _method


def get_category_list(**kwargs) -> dict:
  return _method("GET", "/categories",
      **kwargs
  )


def get_category(
    category_id: int,
    **kwargs
) -> dict:
  return _method("GET", f'/categories/{category_id}',
      **kwargs
  )

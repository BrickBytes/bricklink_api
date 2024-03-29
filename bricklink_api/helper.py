def enumize(obj, enum_type):
  if isinstance(obj, enum_type):
    return obj
  else:
    try:
      return enum_type(obj)
    except ValueError as exc:
      try:
        return enum_type[obj]
      except KeyError:
        pass
      if hasattr(obj, "upper"):
        try:
          return enum_type[obj.upper()]
        except KeyError:
          pass
  raise ValueError(f'{obj!r} is not member of enum type: {enum_type.__name__}')


def norm_params(params: dict, *, func=None) -> dict:
  rparams = {}
  annotations = {}
  if func is not None:
    annotations = func.__annotations__
  for name, value in params.items():
    cls = annotations.get(name)
    if hasattr(value, "value"):  # enum support
      value = value.value
    elif cls in {bool, float, int, str}:
      value = cls(value)
    if value is not None:
      rparams[name] = value
  return rparams or None

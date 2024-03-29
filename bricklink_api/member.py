from . import method as _method


def get_member_rating(
    username: str,
    **kwargs
) -> dict:
  return _method.method(
      _method.Method.GET,
      f'/members/{username}/ratings',
      **kwargs
  )


def get_member_note(
    username: str,
    **kwargs
) -> dict:
  return _method.method(
      _method.Method.GET,
      f'/members/{username}/notes',
      **kwargs
  )


def create_member_note(
    username: str,
    note_resource: dict,
    **kwargs
) -> dict:
  return _method.method(
      _method.Method.POST,
      f'/members/{username}/notes',
      json = note_resource,
      **kwargs
  )


def update_member_note(
    username: str,
    note_resource: dict,
    **kwargs
) -> dict:
  return _method.method(
      _method.Method.PUT,
      f'/members/{username}/notes',
      json = note_resource,
      **kwargs
  )


def delete_member_note(
    username: str,
    **kwargs
) -> dict:
  return _method.method(
      _method.Method.PUT,
      f'/members/{username}/notes',
      **kwargs
  )

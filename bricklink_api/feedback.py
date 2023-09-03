import enum as _enum

from . import method as _method


class Direction(_enum.Enum):
  OUT = "out"
  IN = "in"
  DEFAULT = "in"


def get_feedback_list(
    *,
    direction: Direction = None,
    **kwargs
) -> dict:
  return _method.method(
      _method.Method.GET,
      "/feedback",
      **kwargs
  )


def get_feedback(
    feedback_id: int,
    **kwargs
) -> dict:
  return _method.method(
      _method.Method.GET,
      f'/feedback/{feedback_id}',
      **kwargs
  )


def post_feedback(
    feedback_resource: dict,
    **kwargs
) -> dict:
  return _method.method(
      _method.Method.POST,
      "/feedback",
      json = feedback_resource,
      **kwargs
  )


def reply_feedback(
    feedback_id: int,
    feedback_resource: dict,
    **kwargs
) -> dict:
  return _method.method(
      _method.Method.POST,
      f'/feedback/{feedback_id}/reply',
      json = feedback_resource,
      **kwargs
  )

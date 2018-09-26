import enum as _enum

from .method import method as _method


class Direction(_enum.Enum):
  OUT = "out"
  IN = "in"
  DEFAULT = "out"


class Status(_enum.Enum):
  O = "open"
  S = "redeemed"
  D = "denied"
  E = "expired"
  OPEN = "open"
  REDEEMED = "redeemed"
  DENIED = "denied"
  EXPIRED = "expired"


def get_coupons(
    *,
    direction: Direction = None,
    status: str = None,  #TODO!
    **kwargs
) -> dict:
  params = _helper.norm_params({
      "direction": direction,
      "status": status,
  })
  return _method("GET", "/coupons",
      params = params,
      **kwargs
  )


def get_coupon(
    coupon_id: int,
    **kwargs
) -> dict:
  return _method("GET", f'/coupons/{coupon_id}',
      **kwargs
  )


def create_coupon(
    coupon_resource: dict,
    **kwargs
) -> dict:
  return _method("GET", "/coupons",
      json = coupon_resource,
      **kwargs
  )


def update_coupon(
    coupon_id: int,
    coupon_resource: dict,
    **kwargs
) -> dict:
  return _method("PUT", f'/coupons/{coupon_id}',
      json = coupon_resource,
      **kwargs
  )


def delete_coupon(
    coupon_id: int,
    **kwargs
) -> dict:
  return _method("DELETE", f'/coupons/{coupon_id}',
      **kwargs
  )

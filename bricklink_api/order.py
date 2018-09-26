import enum as _enum

from . import helper as _helper
from .method import method as _method


class Direction(_enum.Enum):
  OUT = "out"
  IN = "in"
  DEFAULT = "in"


class PaymentStatus(_enum.Enum):
  NONE = "None"
  SENT = "Sent"
  RECEIVED = "Received"
  CLEARING = "Clearing"
  RETURNED = "Returned"
  BOUNCED = "Bounced"
  COMPLETED = "Completed"


class Status(_enum.Enum):
  PENDING = "Pending"
  UPDATED = "Updated"
  PROCESSING = "Processing"
  READY = "Ready"
  PAID = "Paid"
  PACKED = "Packed"
  SHIPPED = "Shipped"
  RECEIVED = "Received"
  COMPLETED = "Completed"
  OCR = "OCR"
  NPB = "NPB"
  NPX = "NPX"
  NRS = "NRS"
  NSS = "NSS"
  CANCELLED = "Cancelled"


def get_orders(
    *,
    direction: Direction = None,
    status: str = None,
    filed: bool = None,
    **kwargs
) -> dict:
  params = _helper.norm_params({
      "direction": direction,
      "status": status,
      "filed": filed,
  })
  return _method("GET", f'/orders',
      params = params,
      **kwargs
  )


def get_order(
    order_id: int,
    **kwargs
) -> dict:
  return _method("GET", f'/orders/{order_id}',
      **kwargs
  )


def get_order_messages(
    order_id: int,
    **kwargs
) -> dict:
  return _method("GET", f'/orders/{order_id}/messages',
      **kwargs
  )


def get_order_items(
    order_id: int,
    **kwargs
) -> dict:
  return _method("GET", f'/orders/{order_id}/items',
      **kwargs
  )


def get_order_feedback(
    order_id: int,
    **kwargs
) -> dict:
  return _method("GET", f'/orders/{order_id}/feedback',
      **kwargs
  )


def update_order(
    order_id: int,
    order_resource: dict,
    **kwargs
) -> dict:
  return _method("PUT", f'/orders/{order_id}',
      json = order_resource,
      **kwargs
  )


def update_order_status(
    order_id: int,
    status: Status,
    **kwargs
) -> dict:
  value = _helper.enumize(status, Status).name
  return _method("PUT", f'/orders/{order_id}/status',
      json = {"field" : "status", "value": value},
      **kwargs
  )


def update_payment_status(
    order_id: int,
    payment_status: PaymentStatus,
    **kwargs
) -> dict:
  value = _helper.enumize(payment_status, PaymentStatus).value
  return _method("PUT", f'/orders/{order_id}/status',
      json = {"field" : "payment_status", "value": value},
      **kwargs
  )


def send_drive_thru(
    order_id: int,
    mail_me: bool = None,
    **kwargs
) -> dict:
  return _method("POST", f'/orders/{order_id}/drive_thru',
      params = _helper.norm_params({"mail_me": mail_me}),
      **kwargs
  )

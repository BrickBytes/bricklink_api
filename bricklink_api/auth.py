import json as _json
import pathlib as _pathlib

import requests_oauthlib as _requests_oauthlib


def oauth(
    consumer_key: str,
    consumer_secret: str,
    token_value: str,
    token_secret: str,
  ) -> _requests_oauthlib.OAuth1:
  return _requests_oauthlib.OAuth1(
      client_key = consumer_key,
      client_secret = consumer_secret,
      resource_owner_key = token_value,
      resource_owner_secret = token_secret,
  )


class DefaultOAuth:
  _value = None

  @classmethod
  def get(cls):
    if cls._value is None:
      mydir = _pathlib.Path(__file__).parent
      auth_json = mydir / "auth.json"
      if auth_json.is_file():
        with auth_json.open() as f:
          auth_params = _json.load(f)
      cls.set(
          consumer_key = auth_params["ConsumerKey"],
          consumer_secret = auth_params["ConsumerSecret"],
          token_value = auth_params["TokenValue"],
          token_secret = auth_params["TokenSecret"],
      )
    return cls._value

  @classmethod
  def set(cls, *args, **kwargs):
    if len(args) == 1 and not isinstance(args[0], str):
      cls._value = args[0]
    elif 1 < len(args):
      cls._value = oauth(*args)
    elif kwargs:
      cls._value = oauth(**kwargs)
    else:
      raise ValueError("unable to set OAuth")

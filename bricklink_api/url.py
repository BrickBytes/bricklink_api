import yarl as _yarl


class DefaultBaseUrl:
  _value = "https://api.bricklink.com/api/store/v1/"

  @classmethod
  def get(cls) -> str:
    return cls._value

  @classmethod
  def set(cls, base_url: str) -> None:
    cls._value = base_url


def get(uri:str="", *, base_url:str=None) -> _yarl.URL:
    if base_url is None:
      base_url = DefaultBaseUrl.get()
    uri = str(uri.lstrip("/"))
    return _yarl.URL(base_url)/ uri


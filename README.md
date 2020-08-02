bricklink_api
=============

version 0.0.1 alpha

This is the documentation of the ``bricklink_api`` Python 3 library and scripts.

**At this moment, the content is in an early alpha stage and under constant development.**
**It is also possible that parts of the API will change soon.**


Installation
------------

```bash
$ pip install git+git://github.com/BrickBytes/bricklink_api.git@master
```

Upgrade
-------

```bash
$ pip install git+git://github.com/BrickBytes/bricklink_api.git@master --upgrade
```


Usage
-----

Head to https://www.bricklink.com/v2/api/register_consumer.page to retrieve your API access token information.

### Interactive example
First, create a copy of the `auth.sample.json` named as `auth.json` and then open it with a text editor and fill it with your auth parameter values. Once done, you can start `python` and test the library:

```
>>> import bricklink_api
>>> bricklink_api.catalog_item.get_price_guide("Set", "6335-1", new_or_used="U")
```

### Script example

```python
from bricklink_api.auth import oauth
from bricklink_api.catalog_item import get_price_guide, Type, NewOrUsed

# fill in with your data from https://www.bricklink.com/v2/api/register_consumer.page
consumer_key = "00000000000000000000000000000000"
consumer_secret = "00000000000000000000000000000000"
token_value = "00000000000000000000000000000000"
token_secret = "00000000000000000000000000000000"
auth = oauth(consumer_key, consumer_secret, token_value, token_secret)

# get price guide for a used 42100-1 (Lego Technic Liebherr R 9800)
json_obj = get_price_guide(Type.SET, "42100-1", new_or_used=NewOrUsed.USED, auth=auth)

# json_obj:
# {'data': {'avg_price': '337.4950',
#           'currency_code': 'EUR',
#           'item': {'no': '42100-1', 'type': 'SET'},
#           'max_price': '349.9900',
#           'min_price': '325.0000',
#           'new_or_used': 'U',
#           'price_detail': [{'quantity': 1,
#                             'qunatity': 1,
#                             'shipping_available': True,
#                             'unit_price': '325.0000'},
#                            {'quantity': 1,
#                             'qunatity': 1,
#                             'shipping_available': True,
#                             'unit_price': '349.9900'}],
#           'qty_avg_price': '337.4950',
#           'total_quantity': 2,
#           'unit_quantity': 2},
#  'meta': {'code': 200, 'description': 'OK', 'message': 'OK'}}
```
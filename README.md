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

First, create a copy of the `auth.sample.json` named as `auth.json` and then open it with a text editor and fill it with your auth parameter values. Once done, you can start `python` and test the library:

```
>>> import bricklink_api
>>> bricklink_api.catalog_item.get_price_guide("Set", "6335-1", new_or_used="U")
```

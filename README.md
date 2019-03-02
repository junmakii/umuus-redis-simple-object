
Utilities, tools, and scripts for Python.

umuus-redis-simple-object
=========================

Installation
------------

    $ pip install git+https://github.com/junmakii/umuus-redis-simple-object.git

Example
-------

    $ umuus_redis_simple_object

    >>> import umuus_redis_simple_object

Usage
-----

    import umuus_redis_simple_object

    class Data(umuus_redis_simple_object.RedisObject):
        value = 1

    instance = redis.Redis.from_url('redis://root:PASSWORD@redis:6379/0')
    data = Data(instance=instance)
    data.value += 1

----

    $ redis-cli KEYS '*'
    "MODULE_NAME.Data.value"

    $ redis-cli GET MODULE_NAME.Data.value
    2

Authors
-------

- Jun Makii <junmakii@gmail.com>

License
-------

GPLv3 <https://www.gnu.org/licenses/>
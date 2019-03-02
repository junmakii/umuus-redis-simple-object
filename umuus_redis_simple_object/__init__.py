#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Jun Makii <junmakii@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""Utilities, tools, and scripts for Python.

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

"""
import json
import logging
__version__ = '0.1'
__url__ = 'https://github.com/junmakii/umuus-redis-simple-object'
__author__ = 'Jun Makii'
__author_email__ = 'junmakii@gmail.com'
__author_username__ = 'junmakii'
__keywords__ = []
__license__ = 'GPLv3'
__scripts__ = []
__install_requires__ = [
    'redis>=3.0.1',
]
__dependency_links__ = []
__classifiers__ = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
]
__entry_points__ = {
    'console_scripts':
    ['umuus_redis_simple_object = umuus_redis_simple_object:main'],
    'gui_scripts': [],
}
__project_urls__ = {
    'Documentation': 'https://github.com/junmakii/umuus-redis-simple-object/',
    'Bug Tracker':
    'https://github.com/junmakii/umuus-redis-simple-object/issues',
    'Source Code': 'https://github.com/junmakii/umuus-redis-simple-object/',
}
# __test_suite__ = 'umuus_redis_simple_object:CustomTestLoader'
# __test_loader__ = 'umuus_redis_simple_object:load_suite'
__extras_require__ = {}
__tests_require__ = ['pytest']
__setup_requires__ = ['pytest-runner']
__package_data__ = {}
__python_requires__ = '>=3.4, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'
__include_package_data__ = True
__zip_safe__ = True
__download_url__ = 'https://github.com/junmakii/umuus-redis-simple-object/zipball/master'
__extra_options__ = {}
__all__ = []

logger = logging.getLogger(__name__)


class RedisObject(object):
    def __init__(self, instance=None, prefix=None, **kwargs):
        self._prefix = (prefix
                        or self.__module__ + '.' + self.__class__.__name__)
        self._instance = instance
        for key, value in self._get_attributes().items():
            setattr(self, key, value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def asdict(self):
        return dict([(key.rsplit('.', 1)[-1],
                      json.loads(self._instance.get(key).decode('utf-8')))
                     for _ in self._instance.scan_iter(self._prefix + '*')
                     for key in [_.decode('utf-8')]])

    def _get_attributes(self):
        return {
            key: value
            for _ in dir(self) for key, value in [(_, getattr(self, _))]
            if not key.startswith('_') and value is not None
            and not callable(value)
        }

    def __setattr__(self, name, value):
        if name.startswith('_'):
            return object.__setattr__(self, name, value)
        self._instance.set(self._prefix + '.' + name, json.dumps(value))

    def __getattribute__(self, name):
        try:
            attribute = object.__getattribute__(self, name)
        except AttributeError:
            attribute = None
        if name.startswith('_') or callable(attribute):
            return attribute
        value = self._instance.get(self._prefix + '.' + name)
        if value is None:
            return attribute
        return json.loads(value)

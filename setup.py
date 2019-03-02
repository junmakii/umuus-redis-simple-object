
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def run_tests(self):
        import sys
        import shlex
        import pytest
        errno = pytest.main(['--doctest-modules'])
        if errno != 0:
            raise Exception('An error occured during installution.')
        install.run(self)


setup(
    packages=setuptools.find_packages('.'),
    version='0.1',
    url='https://github.com/junmakii/umuus-redis-simple-object',
    author='Jun Makii',
    author_email='junmakii@gmail.com',
    keywords=[],
    license='GPLv3',
    scripts=[],
    install_requires=['redis>=3.0.1'],
    dependency_links=[],
    classifiers=['Development Status :: 3 - Alpha',
 'Intended Audience :: Developers',
 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
 'Natural Language :: English',
 'Programming Language :: Python',
 'Programming Language :: Python :: 3'],
    entry_points={'console_scripts': ['umuus_redis_simple_object = '
                     'umuus_redis_simple_object:main'],
 'gui_scripts': []},
    project_urls={'Bug Tracker': 'https://github.com/junmakii/umuus-redis-simple-object/issues',
 'Documentation': 'https://github.com/junmakii/umuus-redis-simple-object/',
 'Source Code': 'https://github.com/junmakii/umuus-redis-simple-object/'},
    extras_require={},
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    package_data={},
    python_requires='>=3.4, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    include_package_data=True,
    zip_safe=True,
    download_url='https://github.com/junmakii/umuus-redis-simple-object/zipball/master',
    name='umuus-redis-simple-object',
    description='Utilities, tools, and scripts for Python.',
    long_description=('Utilities, tools, and scripts for Python.\n'
 '\n'
 'umuus-redis-simple-object\n'
 '=========================\n'
 '\n'
 'Installation\n'
 '------------\n'
 '\n'
 '    $ pip install '
 'git+https://github.com/junmakii/umuus-redis-simple-object.git\n'
 '\n'
 'Example\n'
 '-------\n'
 '\n'
 '    $ umuus_redis_simple_object\n'
 '\n'
 '    >>> import umuus_redis_simple_object\n'
 '\n'
 'Usage\n'
 '-----\n'
 '\n'
 '    import umuus_redis_simple_object\n'
 '\n'
 '    class Data(umuus_redis_simple_object.RedisObject):\n'
 '        value = 1\n'
 '\n'
 "    instance = redis.Redis.from_url('redis://root:PASSWORD@redis:6379/0')\n"
 '    data = Data(instance=instance)\n'
 '    data.value += 1\n'
 '\n'
 '----\n'
 '\n'
 "    $ redis-cli KEYS '*'\n"
 '    "MODULE_NAME.Data.value"\n'
 '\n'
 '    $ redis-cli GET MODULE_NAME.Data.value\n'
 '    2\n'
 '\n'
 'Authors\n'
 '-------\n'
 '\n'
 '- Jun Makii <junmakii@gmail.com>\n'
 '\n'
 'License\n'
 '-------\n'
 '\n'
 'GPLv3 <https://www.gnu.org/licenses/>'),
    cmdclass={"pytest": PyTest},
)
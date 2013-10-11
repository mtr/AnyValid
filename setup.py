# coding=utf-8
from distutils.core import setup

setup(
    name='AnyValid',
    version='1.0.0',
    author='Martin Thorsen Ranang',
    author_email='mtr@ranang.org',
    packages=['any_valid', 'any_valid.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/AnyValid/',
    license='LICENSE.txt',
    description='Useful towel-related stuff.',
    long_description=open('README.md').read(),
    install_requires=[
        "formencode >= 1.2.0",
    ],
)

from setuptools import setup, find_packages

setup(
    name='simpleFileCache',
    version='1.0.0',
    author='zackaryW',
    install_requires=['cryptography', 'keyring', 'requests', 'sioDict'],
    packages=[
        'simpleFileCache',
        'simpleFileCache.utils',
    ]
)
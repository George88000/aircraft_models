from setuptools import setup

setup(
    name='aircraft_models',
    version='1.0',
    description='This package contains a list of the Aircraft models and manufacturer as per DOC 8643 ICAO',
    author='Giorgio Scarso',
    author_email='scarso.giorgio@gmail.com',
    py_modules=['data'],
    package_dir={'': '.'},
    install_requires=[]
)
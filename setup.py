from setuptools import setup

setup(
    name='aircraft_models_list',
    version='1.0',
    description='This package contains a list of the Aircraft models and manufacturer as per DOC 8643 ICAO',
    author='Giorgio Scarso',
    author_email='scarso.giorgio@gmail.com',
    packages=['aircraft_models_list'],
    install_requires=['pandas'],
)
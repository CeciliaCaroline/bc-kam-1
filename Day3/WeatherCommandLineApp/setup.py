from setuptools import setup

setup(
    name='Weather App',
    version='1.0',
    py_modules=['index'],
    requires=['Click', 'requests'],
    entry_points={
        'console_scripts': ['begin=index:cli'],
    }
)

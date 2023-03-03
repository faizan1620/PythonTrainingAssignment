from setuptools import setup

setup(
    name='commads',
    version='0.1.0',
    py_modules=['commands'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'switch = switch:cli',
            'main = main:main',
            'restaurant = restaurant:cli',
            'utilalias = utilalias:cli',
            'clearsc = clearsc:cli',
            'weather = weather:weather',
            'convert = convert:cli',
            'calculator = calculator:cli'
        ],
    },
)
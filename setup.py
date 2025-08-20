from setuptools import setup

setup(
    name='zakuro',
    version='0.1',
    py_modules=['zakuro'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        zakuro=zakuro:main
    ''',
)
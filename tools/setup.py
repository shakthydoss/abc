from setuptools import setup
setup(
    name='genie',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'genie=genie:main'
        ]
    }
)

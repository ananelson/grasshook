from setuptools import setup, find_packages
from grasshook.version import GRASSHOOK_VERSION

setup(
        author='Ana Nelson',
        author_email='ana@ananelson.com',
        description='Periodic Data Collection',
        entry_points = {
            'console_scripts' : [
                'grasshook = grasshook.commands:run'
                ]
            },
        include_package_data = True,
        install_requires = [
            "tables>=3.0.0"
            ],
        name='grasshook',
        packages=find_packages(),
        url='http://dexy.it/grasshook',
        version=GRASSHOOK_VERSION
        )

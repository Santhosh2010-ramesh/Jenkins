# setup.py

from setuptools import setup, find_packages

setup(
    name="python-app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List other dependencies here if needed
    ],
    test_suite='pytest',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'python-app = app:greet',
        ],
    },
)

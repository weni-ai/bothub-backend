from setuptools import setup, find_packages


setup(
    name='bothub_backend',
    version='1.0.10',
    description='Bothub NLP Backend',
    packages=find_packages(),
    install_requires=[
        'requests==2.20.1',
    ],
)

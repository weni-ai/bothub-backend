from setuptools import setup, find_packages


setup(
    name='bothub_backend',
    version='1.0.19',
    description='Bothub NLP Backend',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)

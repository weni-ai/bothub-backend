from setuptools import setup, find_packages


setup(
    name='bothub_backend',
    version='develop-1.0.23',
    description='Bothub NLP Backend',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)

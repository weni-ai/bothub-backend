from setuptools import setup, find_packages


setup(
    name='bothub_backend',
    version='1.0.21-hotfix',
    description='Bothub NLP Backend',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)

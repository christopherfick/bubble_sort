from setuptools import setup, find_packages

setup(
    name='bubblesort',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='APOC industries',
    description = 'List sorting tool',
    long_description=open('README.md').read(),
    url='https://github.com/KOMelite/bubblesort',
    author='Christopher Fick',
    author_email='fick.christopher@yahoo.com'
)
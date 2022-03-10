from setuptools import setup, find_packages

setup(
    name = 'mypackage',
    packages = find_packages(exclude = ['tests*']),
    license = 'MIT',
    description = 'EDSA example python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/Royal-Priest/myPackage',
    author ='Royal-Priest',
    author_email ='aromehjoseph0@gmail.com'

)
from setuptools import find_packages
from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name="configmaker",
    version="1.0.0",
    description="This package is a little utility package to generate easy-to-use configuration classes in python from a YAML configuration file.",
    long_description=long_description,
    author="Richard ARNAUD",
    author_email="riri8546@gmail.com",
    url="https://github.com/Jehxon/ConfigurationMaker.git",
    install_requires=['pyyaml'],
    packages=find_packages(exclude=['tests', 'testing']),
    scripts=["config_class_generator.py"],
)

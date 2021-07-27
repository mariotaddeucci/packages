
from setuptools import setup
import yaml
from sys import argv
from os import path


name = argv[2]

with open(f"{name}/README.md", "r") as fh:
    long_description = fh.read()

requirements_uri = f"{name}/requirements.txt"

if path.exists(requirements_uri):
    with open(requirements_uri, "r") as f:
        requirements = f.readlines()
else:
    requirements = []

with open(f"{name}/config.yml", 'r') as stream:
    configs = yaml.safe_load(stream)

setup(
    name=name,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/mariotaddeucci/packages/python/{name}/',
    author='Mario Taddeucci',
    author_email='mariotaddeucci@gmx.com',
    license='MIT',
    packages=[name],
    zip_safe=False,
    install_requires=requirements,
    **configs
)

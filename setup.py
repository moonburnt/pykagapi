from setuptools import find_packages, setup

VERSION = "0.2.0"

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pykagapi",
    version=VERSION,
    description="pykagapi - python wrapper for King Arthur's Gold-related APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moonburnt/pykagapi",
    author="moonburnt <moonburnt@disroot.org",
    license="WTFPL",
    classifiers=["Programming Language :: Python :: 3"],
    packages=find_packages(),
    install_requires=["requests>=2.25.1"],
    )

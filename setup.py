#! /usr/bin/env python

from setuptools import setup

with open("requirements.txt", "r") as f:
    deps = list(map(lambda x: x.strip(), f.readlines()))

setup(
    name="mudyom",
    packages=["mudyom"],
    scripts=["scripts/mudyom-cli"],
    version="0.0.1",
    install_requires=deps,
    description="...",
    author="...",
    author_email="...",
    url="...",
    download_url="...",
    keywords=["tokenization", "gazetteer", "thai"],
    classifiers=[
        "Development Status :: 3 - Alpha"
    ],
)
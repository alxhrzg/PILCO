from setuptools import setup
from setuptools import find_packages

import re
import os
import sys
from pkg_resources import parse_version
from os.path import join, dirname, realpath


def read_requirements_file(filename):
    req_file_path = "%s/%s" % (dirname(realpath(__file__)), filename)
    with open(req_file_path) as f:
        return [line.strip() for line in f]


######################
# Check Version Info #
######################
vi = sys.version_info
assert (
    vi.major >= 3 and vi.minor >= 8
), f"Trying to install for environment with python: python=={vi.major}.{vi.minor}.{vi.micro} but only python>=3.8.x is allowed"

# Dependencies of PILCO
packages = find_packages(".")
setup(
    name="pilco",
    version="0.1",
    author="Nikitas Rontsis, Kyriakos Polymenakos",
    author_email="nrontsis@gmail.com",
    description=("A TensorFlow implementation of PILCO"),
    license="MIT License",
    keywords="reinforcement-learning model-based-rl gaussian-processes tensorflow machine-learning",
    url="http://github.com/nrontsis/PILCO",
    packages=packages,
    install_requires=read_requirements_file("requirements.txt"),
    include_package_data=True,
    test_suite="tests",
    extras_require={"Tensorflow with GPU": ["tensorflow-gpu==1.13.1"]},
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)

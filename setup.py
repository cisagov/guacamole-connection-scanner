"""
This is the setup module for the guacscanner project.

Based on:

- https://packaging.python.org/distributing/
- https://github.com/pypa/sampleproject/blob/master/setup.py
- https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
"""

# Standard Python Libraries
import codecs
from glob import glob
from os.path import abspath, basename, dirname, join, splitext

# Third-Party Libraries
from setuptools import find_packages, setup


def readme():
    """Read in and return the contents of the project's README.md file."""
    with open("README.md", encoding="utf-8") as f:
        return f.read()


# Below two methods were pulled from:
# https://packaging.python.org/guides/single-sourcing-package-version/
def read(rel_path):
    """Open a file for reading from a given relative path."""
    here = abspath(dirname(__file__))
    with codecs.open(join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(version_file):
    """Extract a version number from the given file path."""
    for line in read(version_file).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name="guacscanner",
    # Versions should comply with PEP440
    version=get_version("src/guacscanner/_version.py"),
    description="Scan for EC2 instances added (removed) from a VPC and create (destroy) the corresponding Guacamole connections.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    # Landing page for CISA's cybersecurity mission
    url="https://www.cisa.gov/cybersecurity",
    # Additional URLs for this project per
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#project-urls
    project_urls={
        "Source": "https://github.com/cisagov/guacscanner",
        "Tracker": "https://github.com/cisagov/guacscanner/issues",
    },
    # Author details
    author="Cybersecurity and Infrastructure Security Agency",
    author_email="github@cisa.dhs.gov",
    license="License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        # Pick your license as you wish (should match "license" above)
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires=">=3.9",
    # What does your project relate to?
    keywords="aws, guacamole, vpc",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    # TODO: Loosen these requirements.  See cisagov/guacscanner#9 for
    # more details.
    install_requires=[
        "boto3 == 1.34.108",
        "docopt == 0.6.2",
        "ec2-metadata == 2.13.0",
        "psycopg == 3.1.19",
        "schema == 0.7.7",
        "setuptools",
    ],
    extras_require={
        # IMPORTANT: Keep type hinting-related dependencies of the dev section
        # in sync with the mypy pre-commit hook configuration (see
        # .pre-commit-config.yaml). Any changes to type hinting-related
        # dependencies here should be reflected in the additional_dependencies
        # field of the mypy pre-commit hook to avoid discrepancies in type
        # checking between environments.
        "dev": [
            "types-boto3",
            "types-docopt",
            "types-setuptools",
        ],
        "test": [
            "coverage",
            "coveralls",
            # We are using the moto syntax that debuted in version
            # 5.0.0.
            "moto[ec2] >= 5.0.0",
            "pre-commit",
            "pytest-cov",
            "pytest",
        ],
    },
    # Conveniently allows one to run the CLI tool as
    # `guacscanner`
    entry_points={
        "console_scripts": [
            "guacscanner = guacscanner.guacscanner:main",
        ],
    },
)

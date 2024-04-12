# coding: utf-8


"""
IGNORE:
    Nutanix Licensing Versioned APIs

    licensing desc placeholder  # noqa: E501

    OpenAPI spec version: 4.0.1-beta-1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
import io
import os
from setuptools import setup, find_packages  # noqa: H301

NAME = "ntnx-licensing-py-client"
VERSION = "4.0.1b1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 ~= 1.26", "six ~= 1.16", "certifi >=2020.4.5.1,<=2023.11.17", "python-dateutil ~= 2.8", "pysocks ~= 1.7"]

package_root_path = os.path.abspath(os.path.dirname(__file__))
readme_file_path = os.path.join(package_root_path, "README.md")
with io.open(readme_file_path, encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name=NAME,
    version=VERSION,
    description="Nutanix Licensing Versioned APIs",
    author_email="sdk@nutanix.com",
    url="",
    keywords=["Nutanix", "v4", "SDK", "Nutanix Licensing Versioned APIs"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=readme,
    long_description_content_type="text/markdown",
)

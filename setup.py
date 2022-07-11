from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in icici_integration/__init__.py
from icici_integration import __version__ as version

setup(
	name="icici_integration",
	version=version,
	description="ICICI payment integration",
	author="SOUL ltd",
	author_email="soul@soul.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

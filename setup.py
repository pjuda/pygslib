import setuptools

with open("README.md", "r") as file_handle:
    long_description = file_handle.read()

setuptools.setup(
    name='pygslib',
    version='0.1.0',
    author="Przemyslaw Juda",
    description="Module for reading gslib files to pandas",
    long_description=long_description,
    packages=setuptools.find_packages()
)


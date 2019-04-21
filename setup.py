import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gridcloud",
    version="0.0.1",
    author="Grid Presence",
    author_email="grid.presence@gmx.com",
    description="An abstraction of some AWS interfaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thepresence/gridcloud",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

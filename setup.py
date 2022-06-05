import setuptools

with open("README.MD", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data-utils",
    version="0.0.1",
    author="Tanguy Jooris",
    author_email="tanguy.jooris@hotmail.com",
    description="A bunch of utilities to manipulate data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "main"},
    packages=setuptools.find_packages(where="main"),
    python_requires=">=3.8",  # to be tested with Nox
    requires=["setuptools", "pydantic"]
)

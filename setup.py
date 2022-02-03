import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyStrong",
    version="0.0.5",
    author="Julian Baumgartner",
    author_email="jbaumgartner93@gmail.com",
    description="Type enforcement for python objects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hyptocrypto/Pystrong",
    project_urls={
        "Bug Tracker": "https://github.com/hyptocrypto/Pystrong/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

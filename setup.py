from setuptools import setup, find_packages

setup(
    name="json-module",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, if any
    ],
    author="AmineGm73",
    author_email="aminegazit30@gmail.com",
    description="A module for JSON operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AmineGm73/Json-Module",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

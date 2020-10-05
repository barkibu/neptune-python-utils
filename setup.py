import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neptune-python-utils", # Replace with your own username
    version="2",
    author="AWS",
    author_email="AWS",
    description="AWS neptune python tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/awslabs/amazon-neptune-tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License 2.0"
    ],
    python_requires='>=3.6',
)
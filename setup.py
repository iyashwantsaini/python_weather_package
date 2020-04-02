import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swanweather",
    version="0.0.1",
    author="meyash",
    author_email="yashsn2127@gmail.com",
    description="A weather package. Enter city to get weather.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/yash2127/kernelweather",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rest_helper-dominik@theuerkauf.net",
    version="1.0",
    author="Dominik Theuerkauf",
    author_email="dominik@theuerkauf.net",
    description="A python devops exercise",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires=[
        'configparser', 're', 'docopt', 'threading',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

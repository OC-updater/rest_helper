import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rest_helper-OC-update@bild.dtx.at",
    version="1.02",
    author="OC-Updater",
    author_email="OC-update@bild.dtx.at",
    description="A python devops exercise",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OC-updater/rest_helper.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)

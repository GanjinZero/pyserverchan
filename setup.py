import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyserverchan",
    version="0.0.4",
    author="GanjinZero",
    author_email="yuanz17@mails.tsinghua.edu.cn",
    description="Server-chan for python.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/GanjinZero/pyserverchan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

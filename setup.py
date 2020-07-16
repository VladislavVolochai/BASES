from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()


setup(
    name = 'BASES',
    version = '1.0.0',
    description = 'Conversion of integers into different number systems',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "Volochai Vladyslav",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    keywords = "convert numbers",
    packages = find_packages(),         # список модулей
    install_requires = [], # список пакетов от которых зависит этот пакет
    python_requires = "~=3.2",
    url = ""
    
)

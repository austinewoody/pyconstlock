from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pyconstlock",
    version="0.1.1",  # ⬅️ bump version
    packages=find_packages(),
    description="A simple constant enforcement utility for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Austine Onwubiko",
    url="https://github.com/austinewoody/pyconstlock",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)
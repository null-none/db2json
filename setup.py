from setuptools import setup, find_packages
from codecs import open


try:
    import pypandoc

    long_description = pypandoc.convert("README.md", "rst")
except (IOError, ImportError):
    with open("README.rst", encoding="utf-8") as f:
        long_description = f.read()


setup(
    name="db2json",
    description="This client dumps all* the tables in an sqlite database as json.",
    long_description=long_description,
    keywords="django ipfs storage",
    version="0.1.0",
    author_email="kalinin.mitko@gmail.com",
    url="https://github.com/null-none/db2json",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Framework :: Django",
    ),
    packages=find_packages(),
    install_requires=(
    ),
    setup_requires=("pypandoc",),
)
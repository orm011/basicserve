from setuptools import setup, find_packages

setup(
    name="basicserve",
    version="1.0.0",
    url="git@github.com:orm011/basicserve.git",
    author="Oscar Moll",
    author_email="orm@csail.mit.edu",
    description="serve model in supercloud",
    packages=find_packages(where="basicserve"),
    # install_requires=[],  # installed from environment.yaml
    python_requires=">=3.10",
)

from setuptools import setup, find_packages


required_modules = [
    "flask",
    "gunicorn",
    "keras"]

setup(name="deep-monitoring",
      version="0.0.1",
      packages=find_packages(where="src"),
      package_dir={"":"src"},
      install_requires=required_modules)

from setuptools import setup, find_packages
import os

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="ctrlaltdelusion",
    version="0.0.0",
    author="Bobbylee Ingalls",
    author_email="ingallsbobbylee@yahoo.com",
    description="A Discord bot with AI capabilities",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},  # Add this line
    packages=find_packages(where="src"),  # Update this line
    install_requires=requirements,
    python_requires='>=3.12',
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
)
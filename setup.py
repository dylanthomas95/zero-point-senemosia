from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zps-framework",
    version="0.1.0",
    author="Loris Sichetti, Fabian Leo Naressi",
    author_email="senemosiapuntozero@gmail.com",
    description="Zero Point Senemosì̀a Framework for extracting latent energy in complex organizational systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zps-framework/zps-framework",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "networkx>=2.6",
        "torch>=1.10.0",
        "scikit-learn>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.4",
            "pytest-cov>=2.12.1",
            "black>=21.5b0",
            "flake8>=3.9.2",
            "isort>=5.9.2",
        ],
    },
)

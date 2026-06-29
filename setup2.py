from setuptools import setup, find_packages

setup(
    name="zps-rnn-module",
    version="0.1.0",
    author="Loris Sichetti, Fabian Leo Naressi",
    author_email="senemosiapuntozero@gmail.com",
    description="Graph RNN module for ZPS framework",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch>=1.10.0",
        "numpy>=1.21.0",
        "networkx>=2.6",
    ],
)

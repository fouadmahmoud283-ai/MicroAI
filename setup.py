"""
Setup configuration for MicroPython AI/LLM Library
"""

from setuptools import setup, find_packages

setup(
    name="micropython-ai-llm",
    version="0.1.0",
    description="A MicroPython library for AI/LLM integration",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "micropython-urequests",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: Implementation :: MicroPython",
    ],
)
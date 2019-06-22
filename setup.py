from setuptools import setup, find_packages

setup(
    name="badshell",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "badshell = badshell:main",
        ]
    }
)

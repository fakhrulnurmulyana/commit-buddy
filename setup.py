from setuptools import setup, find_packages

setup(
    name="anmu_buddy",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["typer"],
    entry_points={
        "console_scripts": [
            "anmu_buddy=anmu_buddy.cli:app"
        ]
    }
)
from setuptools import setup, find_packages
from pathlib import Path

README = Path("README.md").read_text(encoding="utf-8")

setup(
    name="ingesta-farmia",
    version="0.1.0",
    description="Motor de ingestas batch (Auto Loader) y streaming (Kafka) para la práctica.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),                # detecta 'ingesta_pkg'
    include_package_data=True,               # permite incluir datos no .py
    package_data={
        "ingesta_pkg": [
            "notebooks/*",                  # incluye tus notebooks
            "images/*",                     # incluye tus imágenes
        ]
    },
    install_requires=[
        "pyspark>=3.3.0",
        "delta-spark>=2.3.0",
        "confluent-kafka>=2.2.0",
    ],
    python_requires=">=3.8",
)
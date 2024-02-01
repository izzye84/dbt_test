from setuptools import find_packages, setup

setup(
    name="dbt_test",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "dbt_test": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-duckdb",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)


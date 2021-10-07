"""Fake log generator setup."""

from setuptools import setup

setup(
    name="fake-logs",
    version="0.1",
    author="Rajesh Yogeshwar",
    author_email="rajesh.yogeshwar@gmail.com",
    description="Tool to generate fake logs for testing and to be used in learning tools like Kafka",
    include_package_data=True,
    url="https://github.com/rajeshyogeshwar/fake-logs",
    license="MIT",
    install_requires=["Click", "pandas", "loguru", "Faker"],
    python_requires=">=3.7",
    entry_points="""
        [console_scripts]
        fake-logs=cli:generate_fake_logs
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

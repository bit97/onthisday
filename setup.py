from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

setup(
    name="onthisday",
    packages=find_packages(include=["onthisday"]),
    version="1.1.0",
    description="Retrieve events that happened on current day",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="bit97",
    author_email="federico.bitondo@gmail.com",
    url="https://github.com/bit97/onthisday",
    download_url="https://github.com/bit97/onthisday/archive/refs/tags/1.1.0.tar.gz",
    keywords=[
        "cli",
        "command-line",
        "wikipedia",
        "scraping",
        "today-widget",
        "today",
        "greetings",
    ],
    license="WTFPL",
    install_requires=["Babel", "beautifulsoup4", "typer"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)

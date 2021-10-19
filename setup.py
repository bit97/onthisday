from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='onthisday',
    packages=find_packages(include=['onthisday']),
    version='0.1.0',
    description='Retrieve events that happened on current day',
    long_description=readme,
    author='bit97',
    author_email='federico.bitondo@gmail.com',
    url='https://github.com/bit97/onthisday',
    license=license,
    install_requires=['Babel', 'beautifulsoup4'],
    setup_requires=[],
    tests_require=[],
    test_suite='tests'
)

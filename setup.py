import pathlib

from setuptools import setup

from scp import VERSION

readme_file = pathlib.Path(__file__).parent.resolve() / 'README.md'
readme_contents = readme_file.read_text()

setup(
    name="SecondaryCoolantProps",
    version=VERSION,
    packages=['scp'],
    description="A collection of secondary coolant fluid property functions and classes",
    install_requires=['click'],
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    author='Matt Mitchell',
    author_email='mitchute@gmail.com',
    url='https://github.com/mitchute/SecondaryCoolantProps',
    license='BSD license',
    entry_points={
        'console_scripts': ['scprop=scp.cli:cli']
    }
)

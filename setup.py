import pathlib
from setuptools import setup


readme_file = pathlib.Path(__file__).parent.resolve() / 'README.md'
readme_contents = readme_file.read_text()

setup(
    name="SecondaryCoolantProps",
    version="0.3",
    packages=['scp'],
    description="A collection of secondary coolant fluid property functions and classes",
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    author='Matt Mitchell',
    author_email='mitchute@gmail.com',
    url='https://github.com/mitchute/SecondaryCoolantProps',
    license='Something',
    entry_points={
        'console_scripts': ['SCProps=scp.cli:main', 'scprop=scp.cli:cli']
    }
)

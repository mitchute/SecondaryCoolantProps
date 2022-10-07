import pathlib
from setuptools import setup


readme_file = pathlib.Path(__file__).parent.resolve() / 'README.md'
readme_contents = readme_file.read_text()

setup(
    name="SecondaryCoolantProps",
    version="0.1",
    packages=['scp'],
    description="A collection of secondary coolant fluid property functions and classes",
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    author='People Person',
    author_email='p@p.p',
    url='https://github.com/mitchute/SecondaryCoolantProps',
    license='Something',
    entry_points={
        'console_scripts': ['scp_cli=scp.main:main_cli']
    }
)

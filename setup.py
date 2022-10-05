import pathlib
from setuptools import setup


readme_file = pathlib.Path(__file__).parent.resolve() / 'README.md'
readme_contents = readme_file.read_text()

setup(
    name="GHE Designer Scaffold",
    version="0.2",
    description="A collection of GHE functions and design tools",
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    author='People Person',
    author_email='p@p.p',
    url='https://github.com/Myoldmopar/ghe-scaffold',
    license='Something',
    entry_points={
        'console_scripts': ['ghe_cli=ghe.main:main_cli']
    }
)

from setuptools import setup, find_packages
from pathlib import Path

with Path('README.md').open(encoding='utf8') as readme:
    readme = readme.read()

setup(
    name='sijuiacion-lang',
    version="0.2.0",
    keywords="",  # keywords of your project that separated by comma ","
    description="",  # a conceise introduction of your project
    long_description=readme,
    long_description_content_type="text/markdown",
    license='mit',
    python_requires='>=3.6.0',
    url='https://github.com/RemuLang/sijuiacion-lang',
    author='thautwarm',
    author_email='twshere@outlook.com',
    packages=find_packages(),
    entry_points={"console_scripts": ['sij=sijuiacion_lang.interface:main']},
    # above option specifies commands to be installed,
    install_requires=["rbnf-rts", 'argser', 'typing_extensions', 'bytecode'],
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)

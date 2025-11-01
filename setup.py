from setuptools import setup
from Cython.Build import cythonize

setup(
    name="heic_converter",
    ext_modules=cythonize(
        "core.py", 
        compiler_directives={"language_level": "3"}
    ),
)
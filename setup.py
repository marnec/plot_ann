import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="plot_ann",
    version="1.0.15",
    description="Plot an Artificial Neural Network (ANN) model",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Marco Necci",
    license="MIT License",
    install_requires=["matplotlib", "numpy"],
    py_modules=['plot_ann'],
)


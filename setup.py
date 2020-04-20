import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="seals-PANNEAU-MIKEC-LOUISON",
    version="0.0.1",
    author="Guilhem PANNEAU, Dimitri MIKEC, Jonathan LOUISON",
    author_email="guilhem.panneau@insa-lyon.fr",
    description="This package allows to model the impact of the sand extraction on 3 species of the Bay of the Somme - seals, soles and lugworms.",
    long_description= "This project allows to return four graph : * graph 1 : The evolution of the number of seals during the duration of the experiment. * graph 2 : The evolution of the number of soles during the duration of the experiment. * graph 3 : The evolution of the number of lugworms during the duration of the experiment. * graph 4 : The evolution of the amount of sand in cubic meters during the duration of the experiment."
    long_description_content_type="text/markdown",
    url="https://github.com/gpanneau/seals",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CeCILL ",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

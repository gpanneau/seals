# Modelization of the impact of the sand extraction on the seal food chain 

seals is a Python 3.7 package allows to model the impact of the sand extraction on 3 species of the Bay of the Somme - seals, soles and lugworms.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

pip install sys
pip install pylab
pip install scipy
pip install numpy


## Installing

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps seals
```

## Features

This project allows to return four graph :
* graph 1 : The evolution of the number of seals during the duration of the experiment.
* graph 2 : The evolution of the number of soles during the duration of the experiment.
* graph 3 : The evolution of the number of lugworms during the duration of the experiment.
* graph 4 : The evolution of the amount of sand in cubic meters during the duration of the experiment.

## TODO

* Allowing the modification of the growth rate of seals, soles and lugworms populations.
* Rectify the rough change of periodicity during the modeling.

## Tutorial

```bash
python tutorial.py
```

is equivalent to :

```bash
python main.py 20 200 0.2
```

## Tests

```bash
python seals.py -v
```

## FAQ

Which version of Python should I use ? You can use Python3.X

May I save the graphics ? Yes, you can save them with matplotlib

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

* **Guilhem PANNEAU** - *Initial work* - [https://github.com/gpanneau](https://github.com/gpanneau)
* **Dimitri MIKEC** - *Contributor* - [https://github.com/Dikec](https://github.com/Dikec)
* **Jonathan LOUISON** - *Contributor* - [https://github.com/jonathanlsn](https://github.com/jonathanlsn)

## License

This project is licensed under the CeCILL License - see the [license.txt](license.txt) file for details

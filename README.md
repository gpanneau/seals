# Seal food chain modelization

Seal is a Python 3.7 package allows to model the impact of the sand extraction on 3 species of the Bay of the Somme - seals, soles and lugworms.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

pip install sys
pip install pylab
pip install scipy
pip install numpy


## Installing

```bash
apt install seals
```

## Using

```bash
python seals.py extraction_period(int) experience_period(int) extraction_rate_by_year(float) 
```

```Python
```

This function return four graph :
_ graph 1 : The evolution of the number of seals during the duration of the experiment.
_ graph 2 : The evolution of the number of soles during the duration of the experiment.
_ graph 3 : The evolution of the number of lugworms during the duration of the experiment.
_ graph 4 : The evolution of the amount of sand in cubic meters during the duration of the experiment.


## Tutorial

```bash
python tutorial.py
```

## Tests

```bash
python test.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors

* **Guilhem PANNEAU** - *Initial work* - [github.com](https://github.com/gpanneau)
* **Dimitri MIKEC** - *Contributor* - [github.com](https://github.com/Dikec)
* **Jonathan LOUISON** - *Contributor* - [github.com](https://github.com/jonathanlsn)

## License

This project is licensed under the CeCILL License - see the [license.txt](license.txt) file for details

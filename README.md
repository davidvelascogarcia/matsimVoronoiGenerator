# MATSim Voronoi Generator: matsimVoronoiGenerator (Python)

[![matsimVoronoiGenerator Homepage](https://img.shields.io/badge/matsimVoronoiGenerator-develop-orange.svg)](https://github.com/davidvelascogarcia/matsimVoronoiGenerator/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/matsimVoronoiGenerator.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/matsimVoronoiGenerator/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/matsimVoronoiGenerator.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/matsimVoronoiGenerator)

- [MATSim Voronoi Generator: matsimVoronoiGenerator (Python)](#matsim-voronoi-generator-matsimvoronoigenerator-python)
  - [Introduction](#introduction)
  - [Running Software](#running-software)
    - [Arguments](#arguments)
  - [Requirements](#requirements)
  - [Status](#status)
  - [Related projects](#related-projects)

## Introduction

`matsimVoronoiGenerator` is a module in `python` language that automate MATSim simulation network image to create Voronoi resource previous xml file generation.

Documentation available on [docs](https://davidvelascogarcia.github.io/matsimConfigGenerator)

## Running Software

1. Run [matsimVoronoiGenerator.py](./programs).

```bash
python3 matsimVoronoiGenerator.py
```

### Arguments

Avaliable arguments allowed:

| Argument | Full  | Simple | Description  |
| -------  |  ---  |  ----  | -----------  |
|  Network  |  --network  |  -n  | Input xml network  |
|  Plans  |  --plans  |  -p  | Input xml plans  |
|  Output  |  --output  |  -o  | Output simulation dir  |

## Requirements

`matsimConfigGenerator` requires:

[Install pip3](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)

```bash
pip3 install -r requirements.txt
```

Tested on: `windows 10`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `kubuntu 20.04`.

## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/matsimVoronoiGenerator.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/matsimVoronoiGenerator)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/matsimVoronoiGenerator.svg?label=Issues)](https://github.com/davidvelascogarcia/matsimVoronoiGenerator/issues)

## Related projects

* [davidvelascogarcia: matsimConfigGenerator (Python)](https://github.com/davidvelascogarcia/matsimConfigGenerator)
* [davidvelascogarcia: matsimDataAdapter (Python)](https://github.com/davidvelascogarcia/matsimDataAdapter)
* [davidvelascogarcia: matsimDataGenerator (Python)](https://github.com/davidvelascogarcia/matsimDataGenerator)
* [davidvelascogarcia: matsimNetGenerator (Python)](https://github.com/davidvelascogarcia/matsimNetGenerator)
* [davidvelascogarcia: matsimPlansGenerator (Python)](https://github.com/davidvelascogarcia/matsimPlansGenerator)
* [davidvelascogarcia: matsimVoronoiGenerator (Python)](https://github.com/davidvelascogarcia/matsimVoronoiGenerator)

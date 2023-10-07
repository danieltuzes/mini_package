# pip package demo

This repo shows a minimal example that can be installed into the [gep_host_service](https://github.com/danieltuzes/gep_host_service).

- [Files and folders](#files-and-folders)
- [Installation and Dependencies](#installation-and-dependencies)
- [Run the program](#run-the-program)
- [program inputs and outputs](#program-inputs-and-outputs)

## Files and folders

The following files and folders are contained within this folder (or will be created during setup or tests):

```text
pip_package_demo
│
│   README.md
│   requirements.txt
│   
├───config
│        MasterConfig.cfg
│        params.cfg
│   
├───data
│        mytable_sample.csv
│   
└───pmdemo_min
        __init__.py
        __main__.py
        my_mod.py
        utils.py

```

This mini package has no setup.py so it cannot be installed, python must run this package from source.

## Installation and Dependencies

I suggest to use the conda package manager to maintain environments. Once you
installed [miniconda](https://docs.conda.io/en/latest/miniconda.html), even as
a user, start an activated prompt (like the Anaconda Prompt), create and
activate a new environment.

The dependencies can be installed by running `pip install requirements` in the root.
The package won't be installed into the environment, therefore execution can be possible only if the python file to execute is explicitely passed to python.

## Run the program

Cd into the root and issue
```python -m pmdemo_min```

The package cannot be executed by `python __main__.py` or by using any filename. The `-m` switch is mandatory, as this package won't be installed.

## program inputs and outputs

For inputs, it takes command line arguments, a so-called masterconfig, contianing all the input and output files. The masterconfig has an inputs section, defining:

1. a data file (csv, database, big)
2. a config file (cfg, text, small)

As outputs, it

1. writes to the outputs
   1. some version information to the stdout,
   2. log messages to stderr. Note that even info or debug levels too go to stderr.
2. Creates output files at the locations where the masterconfig said so
   1. a log file storing the log messages
   2. a result file of this simple model

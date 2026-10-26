TERMINAL.py

A small Python terminal project.

Version: BETA 2.1.1
Status: Beta

About

TERMINAL is a Python-based command-line project with a central terminal interface and separate modules for different functions.

The project combines a terminal interface, a backend storage component, data editing tools and additional utilities.

Components

* Terminal.py – Central terminal interface and command handling
* main.py – Project starter
* dama.py – DAMA backend for data storage and system information
* dve.py – Data Value Editor (DVE), an interface for inspecting and editing DAMA data
* vdc.py – Voltage Divider Calculator, a utility for calculating voltage dividers using resistor values
* ps.py – Program starting functionality
* headlines.py – Utility for standardized section headings
* dv.py - DAMA data viewer so you can see what is inside the data.txt and index.txt file.
* calc.py - a simple python calcualtor

Requirements

* Python 3, and the packages pyfiglet, os, time and random
* A compatible environment for running the project

Running

Run the project’s starter file:

python main.py

Depending on your environment, you may need to use python3 instead.

Data Storage

DAMA uses text files for data storage.

The project uses an index file and a data file to manage stored values.

Note: The data files may contain local user data. Review them before sharing or publishing them.

Status

TERMINAL is currently in beta.

Features and behavior may change as development continues.

License

No license specified yet.

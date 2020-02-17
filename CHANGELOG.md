# Changelog

Used to document all changes from previous releases and collect changes 
until the next release.

# Latest changes

## Minor updates
- The package version number is now available from the info file as `VERSION` and `__version__`.
- The packages `__init__` file checks if the users Python version is supported by this release and prints a warning otherwise. The python version import is renamed from `version_info` to `python_version` to give context to the user when they are importing functions from the main package.

# Version 1.0.0

## Initial Package setup
- Classifiers, copyright, etc are found in `odmltools/info.json` and available via `odmltools/info.py`.
- CI support with Travis and Appveyor have been set up.
- The packages `__init__` file checks if the users Python version is supported by this release and prints a warning otherwise.

## Import datacite script
- the odmltools.importers package contains a conversion tool from a DataCite XML file (kernel version 4) to odML.
- this importer handles the latest datacite namespace (http://datacite.org/schema/kernel-4) by default. Further namespaces can be added via the command line to also ensure conversion of previous DataCite version files.
- on install a command line convenience script `odmlimportdatacite` is set up for this conversion.
- Basic conversion tests with a full DataCite XML file has been added.

# SSW 555 Agile Methods in Software Engineering
[![Build Status](https://travis-ci.org/jj1976/SSW555AgileMethodsCJBS.svg?branch=master)](https://travis-ci.org/jj1976/SSW555AgileMethodsCJBS)

## Project Structure
This GEDCOM parser is structured as follows:

### GedcomParser.py
This is the top-level class that allows you to parse a single (or many) GEDCOM files. It is broken down into a few pieces:

##### Method:
`GedcomParser.parse_gedcom_file(path/to/file)`
##### Result:
List of Dictionaries containing parsed data. `{Individuals, Families}`

##### Method:
`GedcomParser.print_individuals_data(individual_dict, run_validations)`
##### Result:
A Pretty Table containing all of the INDIVIDUAL information in the GEDCOM file, provided the file is valid.
INDIVIDUAL Error log, if `run_validations` is true.

##### Method:
`GedcomParser.print_family_data(family_dict, individual_data, run_validations)`
##### Result:
A Pretty Table containing all of the FAMILY information in the GEDCOM file, provided the file is valid.
FAMILY Error log, if `run_validations` is true.


### /models
The `models` Directory is where our object classes are located. Each object class contains a definition of what
belongs to each model. For instance, the `Individual.py` class defines the following:
```
"id", "name", "gender", "birthday", "age", "alive", "death", "child", "spouse"
```
Each instance of the `Individual`, after running `GedcomParser.parse_gedcom_file(path/to/file)`, should have a value for each one, if defined in a .GED file.

### Prerequisites
Python 3.x +

## Running the tests

Tests are located in the /tests directory. You can run these tests by running `./python -m test` inside of the /tests directory.

### Coding Style
Style follows PEP8 Guidelines.

## Authors

* **Chris Corrado**  - [Chris](https://github.com/ccorrado)
* **Jermaine Jackson**  - [Jermaine](https://github.com/jj1976)
* **Sukitha Ramasundaram**  - [Sukitha](https://github.com/rsukitha)
* **Brian Prais**  - [Brian](https://github.com/55brian55)

See also the list of [contributors](https://github.com/jj1976/SSW555AgileMethodsCJBS/contributors) who participated in this project.


# Json Module

**A Python module for simplifying JSON file operations**

- ## Features

* Reads, writes, and modifies JSON data stored in files.
* Supports basic operations:
    - `ADD`: Adds a new key-value pair or appends a value to a list.
    - `CHANGE`: Updates the value of an existing key or changes all values in a dictionary.
    - `REMOVE`: Deletes a key-value pair or removes items from a list.
    - `GET`: Retrieves the value of a specific key.
* Automatically handles file paths for user convenience.

- ## Installation
    - ### Clone Repository:
    You can easily using git by the following line
```bash
git clone https://github.com/AmineGm73/Json-Module.git
```

    - ### Installing the package:

```bash
pip install .
```

- ## Usage

    - Import the module and necessary classes:

```python
from json_m import json_file, Operation
Utilisez ce code avec précaution.
Perform operations on JSON files:
```

- Perform operations on JSON files:
```python
# Get a value
value = json_file("my_data.json", Operation.GET, key="name")


# Add a new key-value pair
json_file("my_data.json", Operation.ADD, key="age", new_value=30)

# Change a value
json_file("my_data.json", Operation.CHANGE, key="name", new_value="Alice")

# Remove a key-value pair
json_file("my_data.json", Operation.REMOVE, key="age")
Utilisez ce code avec précaution.
```

- ## Additional Notes

The module determines the file path relative to the calling script's directory.
Error handling is incorporated for robustness.
Consider specifying a custom file path if needed.

- ## License

This module is licensed under the MIT License. See the [LICENSE](https://github.com/AmineGm73/Json-Module/blob/main/LICENSE) file for details.

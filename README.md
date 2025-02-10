# JSON to YAML Converter

This Python script converts JSON (JavaScript Object Notation) strings to YAML (YAML Ain't Markup Language) strings.  It utilizes the `json` and `pyyaml` libraries to perform the conversion.

## Features

* **JSON to YAML Conversion:**  Converts valid JSON strings into YAML format.
* **Error Handling:** Gracefully handles invalid JSON input, providing informative error messages.  Also catches potential errors during YAML generation.
* **Customizable Output:** Allows customization of YAML output through:
    * **Indentation:** Controls the indentation level of the YAML output.
    * **Key Sorting:**  Option to sort keys alphabetically in the YAML output.
* **Clear and Readable Code:**  Well-structured and commented code for easy understanding and modification.

## Requirements

* Python 3.x
* `pyyaml` library: Install using `pip install pyyaml`

## Usage

1.  **Save the Script:** Save the provided Python code (e.g., `json_to_yaml.py`).
2.  **Import the Function:**  Import the `json_to_yaml` function into your Python script.
3.  **Call the Function:**  Call the `json_to_yaml` function, passing the JSON string as an argument.

```python
import json
import yaml  # noqa: F401 -- needed to avoid import errors in some IDEs
from json_to_yaml import json_to_yaml

json_data = """
{
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}
"""

yaml_data = json_to_yaml(json_data)

if yaml_data:
  print(yaml_data)

import json
import yaml

def json_to_yaml(json_string, indent=2, sort_keys=False):
  """
  Converts a JSON string to a YAML string.

  Args:
    json_string: The JSON string to convert.
    indent: (Optional) The indentation level for the YAML output. Defaults to 2.
    sort_keys: (Optional) Whether to sort the keys in the YAML output. Defaults to False.

  Returns:
    A YAML string representing the JSON data.
    Returns None if the input JSON is invalid.
  """
  try:
    json_data = json.loads(json_string)
  except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON - {e}")
    return None

  try:
    yaml_string = yaml.dump(json_data, indent=indent, sort_keys=sort_keys)
    return yaml_string
  except yaml.YAMLError as e:
    print(f"Error: Could not convert JSON to YAML - {e}")
    return None

# Example usage:
if __name__ == "__main__":
  json_data = """
  {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "hiking", "coding"],
    "address": {
      "street": "123 Main St",
      "zip": "10001"
    }
  }
  """

  yaml_data = json_to_yaml(json_data)

  if yaml_data:
    print("YAML output:")
    print(yaml_data)

  print("\n--- Example with sorting and custom indent ---\n")

  yaml_data_sorted = json_to_yaml(json_data, indent=4, sort_keys=True)
  if yaml_data_sorted:
    print("YAML output (sorted and indented):")
    print(yaml_data_sorted)

  print("\n--- Example with invalid JSON ---\n")
  invalid_json = "{'name': 'Invalid' "  # Missing closing brace
  yaml_data_invalid = json_to_yaml(invalid_json)  # Will print error and return None

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

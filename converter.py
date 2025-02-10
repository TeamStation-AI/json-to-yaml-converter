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

# README.md
"""
# JSON to YAML Converter

This script converts a JSON file into YAML format.

## Usage

### Install dependencies
```sh
pip install pyyaml
```

### Run the script
```sh
python converter.py input.json output.yaml
```

## Arguments
- `input.json`: Path to the JSON file you want to convert.
- `output.yaml`: Path where the converted YAML file will be saved.

## Example
```sh
python converter.py example.json example.yaml
```

## License
This project is open-source and available for free use.
"""

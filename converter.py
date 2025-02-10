import json
import yaml
import argparse

def json_to_yaml(json_file, yaml_file):
    """Converts a JSON file to YAML format."""
    try:
        with open(json_file, 'r', encoding='utf-8') as jfile:
            data = json.load(jfile)

        with open(yaml_file, 'w', encoding='utf-8') as yfile:
            yaml.dump(data, yfile, default_flow_style=False, allow_unicode=True)

        print(f"Successfully converted {json_file} to {yaml_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON to YAML")
    parser.add_argument("json_file", help="Path to the JSON file")
    parser.add_argument("yaml_file", help="Path to save the YAML output")
    args = parser.parse_args()

    json_to_yaml(args.json_file, args.yaml_file)
  import json
import yaml
import argparse

def json_to_yaml(json_file, yaml_file):
    """Converts a JSON file to YAML format."""
    try:
        with open(json_file, 'r', encoding='utf-8') as jfile:
            data = json.load(jfile)

        with open(yaml_file, 'w', encoding='utf-8') as yfile:
            yaml.dump(data, yfile, default_flow_style=False, allow_unicode=True)

        print(f"Successfully converted {json_file} to {yaml_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON to YAML")
    parser.add_argument("json_file", help="Path to the JSON file")
    parser.add_argument("yaml_file", help="Path to save the YAML output")
    args = parser.parse_args()

    json_to_yaml(args.json_file, args.yaml_file)

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

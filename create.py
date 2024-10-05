import os
import json
import argparse
import yaml


def load_params(params_path):
    with open(params_path, 'r', encoding='utf-8') as file:
        params = json.load(file)
    return params


def create_file(file_path, content, mode=None):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    if mode:
        os.chmod(file_path, int(mode, 8))


def parse_yaml(config):
    yaml_file = config.get("yaml_file")
    output_folder = config.get("output_folder")
    
    with open(yaml_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    def traverse_dict(d, parent_path=''):
        for key, value in d.items():
            if isinstance(value, dict):
                traverse_dict(value, os.path.join(parent_path, key))
            else:
                file_path = os.path.join(output_folder, parent_path, key)
                content = value
                mode = None
                create_file(file_path, content, mode)

    traverse_dict(data)


def main(params_path):
    params = load_params(params_path)
    parse_yaml(params)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YAML Structure to File System Microproject")
    parser.add_argument(
        '--json-path',
        type=str,
        default="params.json",
        help='Path to JSON configuration file'
    )

    args = parser.parse_args()
    main(args.json_path)

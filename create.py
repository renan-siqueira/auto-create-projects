import argparse
from typing import Any, Dict, Optional
from pathlib import Path
import yaml

# Define constant for encoding
ENCODING = 'utf-8'


def load_params(params_path: str) -> Dict[str, Any]:
    """
    Load parameters from a YAML file.

    :param params_path: Path to the YAML file containing parameters.
    :return: Dictionary with the loaded parameters.
    """
    params_file = Path(params_path)
    if not params_file.is_file():
        raise FileNotFoundError(f"YAML file not found: {params_path}")
    
    with params_file.open('r', encoding=ENCODING) as file:
        return yaml.safe_load(file)


def create_file(file_path: Path, content: str, mode: Optional[str] = None) -> None:
    """
    Create a file with the specified content and set optional permissions.

    :param file_path: Path to the file to be created.
    :param content: Content to be written in the file.
    :param mode: Optional file permissions in octal format (e.g., '755').
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the file with the given content
    file_path.write_text(content, encoding=ENCODING)
    
    # Set file permissions if mode is specified
    if mode:
        file_path.chmod(int(mode, 8))


def traverse_and_create_files(data_dict: Dict[str, Any], output_folder: str, parent_path: Optional[Path] = None) -> None:
    """
    Traverse the YAML dictionary and create files based on its structure.

    :param data_dict: YAML dictionary to traverse.
    :param output_folder: Path to the folder where files will be created.
    :param parent_path: Accumulated base path during recursion.
    """
    output_folder = Path(output_folder)

    if parent_path is None:
        parent_path = Path()  # Root of the output folder

    # Access the 'project' key in the YAML
    project_data = data_dict.get('project', {})
    project_name = project_data.get('name')

    if not project_name:
        raise ValueError("Project name is missing in the YAML data.")

    # Create a folder with the project name
    project_folder = output_folder / project_name
    project_folder.mkdir(parents=True, exist_ok=True)

    # Traverse the dictionary structure
    for item in project_data.get('files', []):
        file_path = project_folder / item['path']
        content = item.get('content', '')

        # Create the file with the specified content
        create_file(file_path, content)
        print(f"Created file: {file_path}")

    print(f"All files created in project folder: {project_folder}")


def parse_yaml_and_create_files(config: Dict[str, Any]) -> None:
    """
    Process a YAML file and create files according to its structure.

    :param config: Dictionary containing configuration such as file paths.
    """
    yaml_file = config.get("yaml_file")
    output_folder = config.get("output_folder")

    if not yaml_file or not output_folder:
        raise ValueError("Both 'yaml_file' and 'output_folder' must be specified in the config.")
    
    yaml_file = Path(yaml_file)
    if not yaml_file.is_file():
        raise FileNotFoundError(f"YAML file not found: {yaml_file}")

    with yaml_file.open('r', encoding=ENCODING) as file:
        data = yaml.safe_load(file)

    # Traverse and create files based on the parsed YAML data
    traverse_and_create_files(data, output_folder)


def process_yaml_structure(params_path: str) -> None:
    """
    Main function that loads parameters and processes the YAML file.

    :param params_path: Path to the YAML file containing the parameters.
    """
    params = load_params(params_path)
    parse_yaml_and_create_files(params)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YAML Structure to File System Microproject")
    parser.add_argument(
        '--json-path',
        type=str,
        default="params.yaml",
        help='Path to YAML configuration file'
    )

    args = parser.parse_args()
    process_yaml_structure(args.json_path)

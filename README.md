
# YAML Structure to File System Microproject

This project is designed to create files based on a YAML structure. The YAML file specifies the file structure and content, and the script processes this YAML file, creating the specified files in the designated output folder.

## Requirements

To install the required dependencies, use the following command:

```
pip install -r requirements.txt
```

Alternatively, you can use the provided `.bat` or `.bin` scripts to automatically set up a virtual environment and install the dependencies:

### On Windows:
```
setup_venv.bat
```

### On Linux/Mac:
```
chmod +x setup_venv.bin
./setup_venv.bin
```

## Usage

The script expects a JSON configuration file that contains the following keys:
- `yaml_file`: The path to the YAML file that defines the structure.
- `output_folder`: The folder where the files will be created.

### Running the Script

You can run the script by passing the path to the JSON file as an argument:

```
python create.py --json-path [/path/to/params.json]
```

### JSON Configuration Example

```json
{
    "yaml_file": "structure.yaml",
    "output_folder": "output"
}
```

### YAML Structure Example

```yaml
folder1:
  file1.txt: "Content of file 1"
  file2.txt: "Content of file 2"
folder2:
  subfolder:
    file3.txt: "Content of file 3"
```

## Files Overview

- `create.py`: The main script that processes the YAML file and creates the specified files.
- `params.example.json`: Example JSON file showing how to configure the script.
- `setup_venv.bat`: Script for setting up the virtual environment and installing dependencies on Windows.
- `setup_venv.bin`: Script for setting up the virtual environment and installing dependencies on Linux/Mac.

## License

This project is licensed under the MIT License.

from collections import OrderedDict
import os
import yaml
import argparse
import sys

# Create a custom YAML dumper to insert blank lines and indent nested objects
class CustomYamlDumper(yaml.SafeDumper):
    # Insert blank lines between top-level objects (from https://github.com/yaml/pyyaml/issues/127)
    def write_line_break(self, data=None):
        super().write_line_break(data)

        if len(self.indents) == 1:
            super().write_line_break()

    # Increase indentation for nested objects
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)

# Set the source and destination folders
SRC_FOLDER = "src"
DEST_FOLDER = "hkmd"

# Parse command line arguments
parser = argparse.ArgumentParser(description="Compile HKMD package definitions from source files.")
parser.add_argument("packages", nargs="+", help="List of package names to compile")
parser.add_argument("-v", "--verbose", action="store_true", default=True, help="Print verbose output")

args = parser.parse_args()
package_names = args.packages

# Ensure the destination folder exists, or create it if not
if not os.path.exists(DEST_FOLDER):
    os.makedirs(DEST_FOLDER)

# Iterate over the package names
for package_name in package_names:
    # Initialize lists to store entities
    entities = []

    # Check if the source folder for the package exists
    if not os.path.exists(os.path.join(SRC_FOLDER, package_name)):
        # Print error to stderr
        if args.verbose:
            print(f"Error: Source folder for package '{package_name}' does not exist.", file=sys.stderr)
        continue

    # Iterate over files in the source folder recursively
    for root, dirs, files in os.walk(os.path.join(SRC_FOLDER, package_name)):
        for filename in files:
            file_path = os.path.join(root, filename)
            if args.verbose:
                print(f"Processing {file_path}...")

            # Check if the file is a YAML file
            if file_path.endswith(".yaml"):
                with open(file_path, "r") as file:
                    # Parse the YAML content
                    content = yaml.safe_load(file)

                    # Ensure that the content has name, description, and is_a fields
                    if not content.get("name") or not content.get("description") or not content.get("is_a"):
                        print(f"Error: {file_path} does not define a valid entity")
                        continue

                    # Append to entities
                    entities.append(content)
                    if args.verbose:
                        print(f" - Found entity or relationship: {content['name']}")
                    

    # Sort the entities and relationships by name
    entities.sort(key=lambda x: x["name"])

    # Write the package definition to the destination file
    dest_file_path = os.path.join(DEST_FOLDER, f"{package_name}.yaml")
    with open(dest_file_path, "w") as file:
        yaml.dump(entities, file, Dumper=CustomYamlDumper, default_flow_style=False, sort_keys=False, allow_unicode=True, width=200)

    if args.verbose:
        print(f"Package definition written to {dest_file_path}")
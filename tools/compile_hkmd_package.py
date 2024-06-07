from collections import OrderedDict
import os
import yaml
import argparse
import sys

# Define a custom YAML representer to preserve key order
def represent_ordereddict(dumper, data):
    value = []
    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        value.append((node_key, node_value))
    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)

yaml.add_representer(OrderedDict, represent_ordereddict)

# Set the source and destination folders
SRC_FOLDER = "src"
DEST_FOLDER = "hkmd"

# Initialize argument parser
parser = argparse.ArgumentParser(description="Compile HKMD package definitions from source files.")
parser.add_argument("packages", nargs="+", help="List of package names to compile")

# Add verbose argument with default of true
parser.add_argument("-v", "--verbose", action="store_true", default=True, help="Print verbose output")

# Parse command-line arguments
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

    # Create the package definition in HKMD format
    # package_definition = OrderedDict([
    #     ("format", "hkmd"),
    #     ("entities", entities),
    #     ("relationships", relationships)
    # ])

    # Write the package definition to the destination file
    dest_file_path = os.path.join(DEST_FOLDER, f"{package_name}.yaml")
    with open(dest_file_path, "w") as file:
        yaml.dump(entities, file, default_flow_style=False, sort_keys=False)

    if args.verbose:
        print(f"Package definition written to {dest_file_path}")
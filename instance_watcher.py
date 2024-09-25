# instance_watcher.py

import json
import os

# Function to get mod loader name based on type
def get_mod_loader_name(mod_loader_type):
    loader_names = {
        1: "forge",
        2: "unknown",
        3: "unknown",
        4: "fabric",
        5: "quilt"
        # Add more types if needed
    }
    return loader_names.get(mod_loader_type, "unknown")

# Function to extract desired fields
def extract_instance_info(source_path, destination_path):
    try:
        # Read the source JSON file
        with open(source_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Extract mod loader type and name
        mod_loader = data.get("baseModLoader")
        if mod_loader is not None:
            mod_loader_type = mod_loader.get("type", 0)
            mod_loader_name = get_mod_loader_name(mod_loader_type)
            modloader_version = mod_loader.get("forgeVersion")
            game_version = data.get("gameVersion")
        else:
            mod_loader_name = "vanilla"
            modloader_version = None
            game_version = data.get("gameVersion")

        # Extract the relevant fields
        extracted_data = {
            "project_name": data.get("name"),
            "mod_loader": mod_loader_name,
            "game_version": game_version,
            "modloader_version": modloader_version,
            "allocated_memory": data.get("allocatedMemory", 0)
        }

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

        # Write the extracted data to the destination JSON file
        with open(destination_path, 'w', encoding='utf-8') as file:
            json.dump(extracted_data, file, indent=4)

        print(f"Extracted information successfully saved to {destination_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    source_file_path = "minecraftinstance.json"  # Source JSON file
    destination_file_path = "instance/instance.json"  # Destination for extracted data
    extract_instance_info(source_file_path, destination_file_path)

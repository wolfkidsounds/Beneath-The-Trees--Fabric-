import json
import os

# Function to extract mod information
def extract_mod_info(source_path, destination_path):
    try:
        # Read the source JSON file
        with open(source_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Initialize the mods list
        mods_list = []

        # Extract mods information
        installed_addons = data.get("installedAddons", [])
        for addon in installed_addons:
            mod_entry = {
                "name": addon.get("name"),
                "id": addon.get("addonID"),
                "file": addon.get("fileNameOnDisk"),
                "url": addon.get("webSiteURL"),
                "download": addon.get("installedFile", {}).get("downloadUrl")
            }
            mods_list.append(mod_entry)  # Append each mod entry to the mods list

        # Write the mods list to the destination JSON file
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        with open(destination_path, 'w', encoding='utf-8') as file:
            json.dump(mods_list, file, indent=4)

        print(f"Extracted mod information successfully saved to {destination_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the source and destination file paths
    source_file_path = "minecraftinstance.json"  # Update this to the correct path
    destination_file_path = "instance/mods.json"  # Update this to your desired output path
    extract_mod_info(source_file_path, destination_file_path)

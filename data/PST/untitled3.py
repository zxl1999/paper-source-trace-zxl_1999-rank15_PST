import os
import xml.etree.ElementTree as ET

# Function to extract title from an XML file
def extract_title(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # The namespace
        ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

        # Find the title
        title = root.find('.//tei:title[@type="main"]', ns).text

        return title
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None

# Path to the directory containing XML files
xml_directory = 'paper-xml'

# Dictionary to store file names and titles
file_titles = {}

# Iterate through all files in the directory
for file_name in os.listdir(xml_directory):
    if file_name.endswith('.xml'):
        file_path = os.path.join(xml_directory, file_name)
        title = extract_title(file_path)
        if title:
            file_titles[file_name] = title

# Print the results
for file_name, title in file_titles.items():
    print(f"File: {file_name}, Title: {title}")
    
# Path to save the JSON file
json_file_path = 'file_titles.json'

# Write the dictionary to a JSON file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(file_titles, json_file, ensure_ascii=False, indent=4)

print(f"Titles extracted and saved to {json_file_path}")


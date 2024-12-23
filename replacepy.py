'''
replace the old text with new specified text for all 
the notebooks in the given directory 

replacepy.py requests the folder path, old and new text from
the user
'''
import os
import json

def replace_in_ipynb(file_path, old_str, new_str):
    """
    Replace all occurrences of old_str with new_str in the given .ipynb file.
    
    Parameters:
    - file_path: Path to the .ipynb file
    - old_str: String to be replaced
    - new_str: String to replace with
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = json.load(f)

    modified = False
    for cell in content.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            modified_source = [line.replace(old_str, new_str) for line in source]
            if modified_source != source:
                cell['source'] = modified_source
                modified = True

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2)
        print(f"Replaced '{old_str}' with '{new_str}' in {file_path}")
    else:
        print(f"No changes made to {file_path}")

def process_directory(directory, old_str, new_str):
    """
    Recursively process all .ipynb files in the given directory.
    
    Parameters:
    - directory: Path to the directory to be processed
    - old_str: String to be replaced
    - new_str: String to replace with
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.ipynb'):
                file_path = os.path.join(root, file)
                replace_in_ipynb(file_path, old_str, new_str)

if __name__ == "__main__":
    directory = input("Enter the directory to process: ")
    old_str = input("Input the old string ")
    new_str = input("Input the new string ")
    
    process_directory(directory, old_str, new_str)

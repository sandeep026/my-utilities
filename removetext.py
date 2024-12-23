'''
removes the specified text from all the notebooks in the
given directory 

removetext.py requests the folder path and text to be 
removed from each notebook file in the given folder
'''
import os
import json

def remove_text_in_code_cells(file_path, text_to_remove):
    """
    Remove the specified text from code cells in the given .ipynb file.
    
    Parameters:
    - file_path: Path to the .ipynb file
    - text_to_remove: Text to remove from code cells
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = json.load(f)

    modified = False
    for cell in content.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            modified_source = [line.replace(text_to_remove, '') for line in source]
            if modified_source != source:
                cell['source'] = modified_source
                modified = True

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2)
        print(f"Removed text '{text_to_remove}' in {file_path}")
    else:
        print(f"No changes made to {file_path}")

def process_directory(directory, text_to_remove):
    """
    Recursively process all .ipynb files in the given directory to remove the specified text from code cells.
    
    Parameters:
    - directory: Path to the directory to be processed
    - text_to_remove: Text to remove from code cells
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.ipynb'):
                file_path = os.path.join(root, file)
                remove_text_in_code_cells(file_path, text_to_remove)

if __name__ == "__main__":
    directory = input("Enter the directory to process: ")
    text_to_remove = input("Enter the text to remove from code cells: ")
    
    process_directory(directory, text_to_remove)

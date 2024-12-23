''' 
convert all notebooks to python files in a given directory

Given the following files,

/folder/file.ipynb
/folder/file.ipynb

note2py creates

/folder/python_files/1.py
/folder/python_files/2.py

'''

import os
import nbformat

def extract_code_from_ipynb(notebook_path):
    """
    Extracts code cells from a Jupyter notebook file.
    
    Parameters:
    - notebook_path: Path to the .ipynb file
    
    Returns:
    - code: A string containing all the code from the notebook's code cells
    """
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    code = ""
    for cell in nb.cells:
        if cell.cell_type == 'code':
            code += cell.source + '\n\n'
    
    return code

def convert_ipynb_to_py(directory):
    """
    Converts all .ipynb files in the given directory to .py files containing only code cells.
    
    Parameters:
    - directory: Path to the directory containing .ipynb files
    """
    output_dir = os.path.join(directory, 'python_files')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    file_counter = 1
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.ipynb'):
                notebook_path = os.path.join(root, file)
                code = extract_code_from_ipynb(notebook_path)
                if code.strip():  # Only create a .py file if there is code
                    py_file_path = os.path.join(output_dir, f"{file_counter}.py")
                    with open(py_file_path, 'w', encoding='utf-8') as f:
                        f.write(code)
                    print(f"Created {py_file_path}")
                    file_counter += 1

if __name__ == "__main__":
    directory = input("Enter the directory containing .ipynb files: ")
    convert_ipynb_to_py(directory)

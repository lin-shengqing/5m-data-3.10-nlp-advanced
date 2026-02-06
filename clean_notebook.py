import nbformat

def clean_notebook(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Remove the widgets metadata
    if 'widgets' in nb.metadata:
        del nb.metadata['widgets']
    
    with open(file_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

clean_notebook('assignment.ipynb')
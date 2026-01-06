#!/usr/bin/env python3
import sys
import nbformat
from nbformat import v4

def normalize(path):
    with open(path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    nb = v4.new_notebook(
        metadata=nb.metadata,
        cells=[
            v4.new_markdown_cell(cell.source) if cell.cell_type == "markdown"
            else v4.new_code_cell(cell.source, outputs=[], execution_count=None)
            for cell in nb.cells
        ],
    )

    with open(path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

if __name__ == "__main__":
    for notebook in sys.argv[1:]:
        normalize(notebook)

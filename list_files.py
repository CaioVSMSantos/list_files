import os
import pathlib

# Current directory
path = pathlib.Path(__file__).parent.resolve()

with open("files_list.txt", "w", encoding="utf-8") as f:
    for root, dirs, files in os.walk(path):
        level = root.replace(str(path), '').count(os.sep)
        indent = ' ' * 4 * (level)

        f.write(f"{indent}{os.path.basename(root)}" + "\n")

        subindent = ' ' * 4 * (level + 1)
        for file in files:
            f.write(f"{subindent}{file}" + "\n")
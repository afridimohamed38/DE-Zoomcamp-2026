from pathlib import Path

current_dir = Path.cwd() #get current pwd this is an iterable object
current_file = Path(__file__).name # get file name

print(f"Files in {current_dir}:")


for filepath in current_dir.iterdir():
    # filepath looks like /workspaces/DE-Zoomcamp-2026/test/file2.txt
    # filepath.name looks like file2.txt

    if filepath.name == current_file:
        continue
    
    print(f" - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f"    content: {content}")


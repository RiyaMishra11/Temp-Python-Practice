"""95 - File Organizer"""
from pathlib import Path
import shutil

def organize_directory(directory):
    directory = Path(directory)
    if not directory.exists():
        raise FileNotFoundError(directory)

    moved = 0
    for file in directory.iterdir():
        if not file.is_file() or file.name.startswith("."):
            continue

        extension = file.suffix.lower().lstrip(".") or "no_extension"
        target = directory / extension
        target.mkdir(exist_ok=True)

        destination = target / file.name
        if destination.exists():
            destination = target / f"{file.stem}_copy{file.suffix}"

        shutil.move(str(file), str(destination))
        moved += 1

    return moved

def main():
    folder = input("Folder to organize: ").strip()
    try:
        print(f"Organized {organize_directory(folder)} file(s).")
    except FileNotFoundError:
        print("Folder not found.")

if __name__ == "__main__":
    main()

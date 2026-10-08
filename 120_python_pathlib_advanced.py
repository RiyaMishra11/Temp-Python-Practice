# 120 Advanced pathlib
from pathlib import Path

print("1.",Path.cwd())

root=Path("/mnt/data/pathlib_120")
root.mkdir(exist_ok=True)
print("2.",root.exists())

file=root/"notes.txt"
file.write_text("Python\nGitHub\nPractice",encoding="utf-8")
print("3.",file)

print("4.",file.read_text(encoding="utf-8"))
print("5.",file.name,file.stem,file.suffix)
print("6.",file.parent)

for i in range(1,4):
    (root/f"file_{i}.txt").write_text(f"Content {i}",encoding="utf-8")
print("7.",[p.name for p in root.glob("*.txt")])

nested=root/"nested"
nested.mkdir(exist_ok=True)
(nested/"data.txt").write_text("Nested",encoding="utf-8")
print("8.",[p.name for p in root.rglob("*.txt")])

old=root/"file_1.txt"
new=root/"renamed.txt"
old.rename(new)
print("9.",new.exists())

print("10.",file.stat().st_size,"bytes")

source=root/"organizer"
source.mkdir(exist_ok=True)
for name in ["a.py","b.py","notes.txt","readme.md"]:
    (source/name).write_text("sample",encoding="utf-8")
folders={".py":source/"python",".txt":source/"text",".md":source/"markdown"}
for folder in folders.values(): folder.mkdir(exist_ok=True)
for item in source.iterdir():
    if item.is_file() and item.suffix in folders:
        item.rename(folders[item.suffix]/item.name)
print("11.",{k:[p.name for p in v.iterdir()] for k,v in folders.items()})

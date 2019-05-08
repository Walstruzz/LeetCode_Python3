import os

if os.path.isfile("README.md"):
    os.remove("README.md")

for file in os.listdir("."):
    if not file.endswith(".md"):
        continue
    with open( file, encoding="utf-8") as f:
        lines = f.readlines()
    if lines[0].startswith("---"):
        continue
    title = lines[0][5:].strip()
    top, title = title.split(".")
    add_line = ("---\n"
                       "title: {}\n"
                       "top: {}\n"
                       "categories: Leetcode_python3\n"
                       "---\n").format(".".join([top, title]), top)
    lines = [add_line] + lines
    with open(file, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
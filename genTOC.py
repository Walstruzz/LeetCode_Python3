import os
import os.path

write = []
for file in os.listdir("."):
    name, ext = os.path.splitext(file)
    if name[0].isdigit() and ext == ".md":
        with open(file) as f:
            line = f.readline()
            title = line[line.index("[")+1:line.index("]")]
            section = title.split(".")
            section[0] = section[0].zfill(3)
            title = ".".join(section)
        write.append("- " + "[" + title + "](" + file + ")")
        
if len(write) > 0:
    with open("TOC.md", "w") as f:
        for line in write:
            f.write(line)
            f.write("\n")
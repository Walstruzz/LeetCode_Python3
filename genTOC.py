import os
import os.path

fill_nums = 4
for file in os.listdir("."):
    name, ext = os.path.splitext(file)
    if name[0].isdigit() and ext == ".md":
        with open(file, "r") as f:
            contents = f.readlines()
            title = contents[0][5:]
            digits, title = title.split(".")
            digits = digits.zfill(fill_nums)
            title = "#### " + ".".join([digits, title])
            contents[0] = title
        with open(file, "w") as f:
            for line in contents:
                f.write(line)

files = os.listdir(".")
for file in files:
    name, ext = os.path.splitext(file)
    if name[0].isdigit() and ext == ".md":
        name_list = [n for n in file.split(".") if len(n)]
        name_list[0] = name_list[0].zfill(fill_nums)
        name = ".".join(name_list)
        os.rename(file, name)

write = []
for file in os.listdir("."):
    name, ext = os.path.splitext(file)
    if name[0].isdigit() and ext == ".md":
        with open(file, "r") as f:
            line = f.readline()
            title = line.strip("# \n")
            section = title.split(".")
            section[0] = section[0].zfill(fill_nums)
            title = ".".join(section)
        write.append("- " + "[" + title + "](" + file + ")")

write.sort()
if len(write) > 0:
    with open("TOC.md", "w") as f:
        for line in write:
            f.write(line)
            f.write("\n")

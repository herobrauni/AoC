import string
import sys
import os

with open("code.py.template", "r") as f:
    template_text = f.read()

day = int(sys.argv[1])
day_for_folder = "0" + str(day) if int(day) < 10 else str(day)

data = {
    "day": day,
    "year": sys.argv[2],
    "day_for_folder": day_for_folder
}

template = string.Template(template_text)
result = template.substitute(data)


with open(os.getcwd() + "/" + data["year"] + "/" + data["day_for_folder"] + "/code.py", "w") as f:
    f.write(result)

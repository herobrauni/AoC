import string
import sys

with open("code.py.template", "r") as f:
    template_text = f.read()

data = {
    "day": sys.argv[1],
    "year": sys.argv[2],
}

template = string.Template(template_text)
result = template.substitute(data)

print(result)

# with open("new_script.py", "w") as f:
#     f.write(result)

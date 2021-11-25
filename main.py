from bs4 import BeautifulSoup
import re
from RLCS.func_detail import FuncDetail

filename = "cheatsheet.txt"
# with open(filename) as fp:
    # soup = BeautifulSoup(fp, 'html.parser')

ret_type_pattern = r"^([a-zA-Z0-9]{2,8})(\s\*+)?"
fn_name_pattern  = r"[A-Z][a-zA-Z]+\(.+\);"
description_pattern = r"(\/\/\s)(.+)"

details = []

with open(filename, "r") as fh:
    lines = fh.readlines()
    for line in lines:
        type_match = [ list(l) for l in re.findall(ret_type_pattern, line) ]
        fn_name_match = re.findall(fn_name_pattern, line)
        description_match = [list(l) for l in list(re.findall(description_pattern, line))]

        fd = FuncDetail()

        if description_match:
            fd.description = description_match[0][1]

        if type_match:
            fd.return_type = type_match[0][0]

        if fn_name_match:
            fd.fn_name = fn_name_match[0]

        details.append(fd)

for d in details:
    if d.return_type != None:
        print(f"{d.return_type} {d.fn_name} {d.description}")


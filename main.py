from bs4 import BeautifulSoup
import re
from RLCS.func_detail import FuncDetail

filename = "cheatsheet.txt"
# with open(filename) as fp:
    # soup = BeautifulSoup(fp, 'html.parser')

ret_type_pattern = r"^([a-zA-Z0-9]{2,8})(\s\*+)?"
fn_name_pattern  = r"([A-Z][a-zA-Z]+)"
description_pattern = r"(\/\/\s)(.+)"

details = []

with open(filename, "r") as fh:
    lines = fh.readlines()
    for line in lines:
        type_match = re.search(ret_type_pattern, line)
        # fn_name_match = re.search(fn_name_pattern, line)
        description_match = [list(l) for l in list(re.findall(description_pattern, line))]

        if description_match:
            fd = FuncDetail()
            fd.description = description_match[0][1]

            details.append(fd)


# for d in details:
    # print(d.description)


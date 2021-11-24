from bs4 import BeautifulSoup
import re
from RLCS.func_detail import FuncDetail

filename = "cheatsheet.txt"
# with open(filename) as fp:
    # soup = BeautifulSoup(fp, 'html.parser')

ret_type_pattern = r"^([a-zA-Z0-9]{2,8})(\s\*+)?"
fn_name_pattern  = r"([A-Z][a-zA-Z]+)"
description_pattern = r"(\/\/\s)([A-Za-z]+\s?\w*)"

details = []

with open(filename, "r") as fh:
    lines = fh.readlines()
    for line in lines:
        type_match = re.search(ret_type_pattern, line)
        fn_name_match = re.search(fn_name_pattern, line)
        description_match = re.split(description_pattern, line)

        print(description_match)

        # fd = FuncDetail("a","b", "c")

        # if type_match is not None:
            # fd.return_type = type_match.group(0)
            # fd.fn_name = fn_name_match.group(0)
            # fd.description = description_match.group(0)

        # details.append(fd)


for detail in details:
    if detail.return_type != "a":
        print(f"{detail.return_type} {detail.fn_name}")

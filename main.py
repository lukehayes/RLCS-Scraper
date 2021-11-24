from bs4 import BeautifulSoup
import re

filename = "cheatsheet.txt"
# with open(filename) as fp:
    # soup = BeautifulSoup(fp, 'html.parser')

line_pattern = "r[a-z]{2,7}"

with open(filename, "r") as fh:
    lines = fh.readlines()
    for line in lines:
        matches = re.match(line_pattern, line)
        print(matches)

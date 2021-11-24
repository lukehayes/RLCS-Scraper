from bs4 import BeautifulSoup

filename = "cheatsheet.txt"
# with open(filename) as fp:
    # soup = BeautifulSoup(fp, 'html.parser')

with open(filename, "r") as fh:
    lines = fh.readlines()

    for line in lines:
        print(line)

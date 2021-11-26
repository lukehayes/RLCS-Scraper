import json
from RLCS.func_detail import FuncDetail
from RLCS.color import Color
from RLCS.terminal import Terminal

with open("cheatsheet.json") as fh:
    data = json.load(fh)

cs_json = data["data"]

for line in cs_json:
    Color.magenta(line['return_type'])
    Color.green(line['function_name'])
    Terminal.arrow();
    Color.yellow(line['description'])
    Color.end()


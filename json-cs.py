import json
from RLCS.func_detail import FuncDetail

with open("cheatsheet.json") as fh:
    data = json.load(fh)

cs_json = data["data"]

for line in cs_json:
    print(f"{line['return_type']} {line['function_name']}")
    print(f"\t {line['description']}")
    print(f"\n")


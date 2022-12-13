#!/usr/bin/python3

import json

inp = input()
data = json.loads(inp)
new_data = {}
new_data["include"] = []
for el in data.get("include"):
    names = el.get("name")
    boards = el.get("board")
    shields = el.get("shield")
    if type(names) != list:
        names = [names]
    if type(boards) != list:
        boards = [boards]
    if type(shields) != list:
        shields = [shields]
    for name in names:
        for board in boards:
            for shield in shields:
                new_el = {}
                if name is not None:
                    new_el["name"] = name.replace(" ", "\ ")
                    new_el["file_name_suffix"] = "-" + name.replace(" ", "-").lower()
                else:
                    new_el["file_name_suffix"] = ""
                new_el["board"] = board
                if shield is not None:
                    new_el["shield"] = shield
                new_data["include"].append(new_el)
print(json.dumps(new_data))

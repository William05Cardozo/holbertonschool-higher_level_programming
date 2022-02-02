#!/usr/bin/python3
"""Script that adds alll arguments to a Python list"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""Name of file"""


filename = "add_items.json"

try:
    json_list = load_from_json_file(filename)
except:
    json_list = []

for argu in sys.argv[1:]:
    json_list.append(argu)

save_to_json_file(json_list, filename)

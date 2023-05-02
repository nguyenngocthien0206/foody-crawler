import json
import ndjson

json_list = ['categories', 'dishes', 'restaurants']

for file in json_list:
    json_file = open(f"json\\{file}.json")
    data = json.load(json_file)
    with open(f"ndjson\\{file}.ndjson", 'w', encoding='utf-8') as outfile:
        output = ndjson.dumps(data)
        outfile.write(output)
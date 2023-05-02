import json

input = open('json\\restaurant_id.json')
data = json.load(input)
jsonArray = []

for row in data:
    if (len(row["dishes"]) != 0):
        jsonArray.append(row)

json_dumps = json.dumps(jsonArray,indent = 4)
with open("json\\restaurants.json", "w") as outfile:
    outfile.write(json_dumps)
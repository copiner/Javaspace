
import json, pickle
d = dict(name='francis', age=20, score=78)
json_str = json.dumps(d)
print(json_str)
json_type = json.loads(json_str)
print(json_type)


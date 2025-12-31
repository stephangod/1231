import json
json_text = """
{
  "title": "AI 산업 동향",
  "views": 1200,
  "tags": ["AI", "미디어", "자동화"]
}
"""

data = json.loads(json_text)
print(data)
print(type(data))

print(data["title"])
print(data["tags"][0])

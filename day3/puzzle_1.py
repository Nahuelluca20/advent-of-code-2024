import re

with open("puzzle_3_input.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()


pattern = r"mul\((\d+),\s*(\d+)\)"


coincidences = re.findall(pattern, raw_text)

results = 0

for c in coincidences:
    mul = int(c[0]) * int(c[1])
    results = results + mul

print(results)

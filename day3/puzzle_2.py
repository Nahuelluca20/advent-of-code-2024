import re

with open("puzzle_3_input.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()


instruction_pattern = r"(do\(\)|don't\(\)|mul\((\d+),\s*(\d+)\))"

instructions = re.findall(instruction_pattern, raw_text)

enabled = True
coincidences = []

for instruction in instructions:
    command = instruction[0]

    if command == "don't()":
        enabled = False
    elif command == "do()":
        enabled = True
    elif command.startswith("mul(") and enabled:
        coincidences.append((instruction[1], instruction[2]))


results = 0
for c in coincidences:
    mul = int(c[0]) * int(c[1])
    results = results + mul

print(results)

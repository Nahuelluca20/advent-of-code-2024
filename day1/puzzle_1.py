with open("puzzle_1_input.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

col1 = []
col2 = []

for line in raw_text.splitlines():
    columns = line.split()
    if len(columns) >= 2:
        col1.append(columns[0])
        col2.append(columns[1])

col1 = sorted(list(map(int, col1)))
col2 = sorted(list(map(int, col2)))

tolal_sum = 0

for idx, num in enumerate(col1):
    # print(num, idx, col2[idx])
    distance = num - col2[idx]
    tolal_sum = tolal_sum + abs(int(distance))

print(tolal_sum)

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

similarity_score = 0
for num in col1:
    total_appears = 0
    for num_col2 in col2:
        if num == num_col2:
            total_appears += 1
    similarity_score = similarity_score + (num * total_appears)
    total_appears = 0

print(similarity_score)

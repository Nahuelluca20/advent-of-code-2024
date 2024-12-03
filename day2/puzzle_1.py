with open("puzzle_2_input.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

array_data = [list(map(int, line.split())) for line in raw_text.splitlines()]

safe_reports = 0


for report in array_data:
    is_increasing = report[0] < report[1]
    is_safe = True

    for i in range(1, len(report)):
        prev = report[i - 1]
        curr = report[i]

        # Check if the order is consistent (ascending or descending)
        if (is_increasing and prev > curr) or (not is_increasing and prev < curr):
            is_safe = False
            break  # Terminate the loop early if it is not safe

        # Check if the difference is outside the allowable range
        if not (1 <= abs(prev - curr) <= 3):
            is_safe = False
            break  # Terminate the loop early if it is not safe

    if is_safe:
        safe_reports += 1  # Safe sum using composite operator

print(safe_reports)

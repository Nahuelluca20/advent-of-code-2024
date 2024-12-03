with open("puzzle_2_input.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Convert input to a list of lists
array_data = [list(map(int, line.split())) for line in raw_text.splitlines()]


def is_safe(report):
    """Returns True if the report is safe according to the original rules."""
    is_increasing = report[0] < report[1] if len(report) > 1 else True
    for i in range(1, len(report)):
        prev = report[i - 1]
        curr = report[i]

        # Check for consistent ordering
        if (is_increasing and prev > curr) or (not is_increasing and prev < curr):
            return False

        # Check if the difference is within the allowable range
        if not (1 <= abs(prev - curr) <= 3):
            return False

    return True


def check_report_with_one_removal(report):
    """Checks if removing one level from the report can make it safe."""
    for i in range(len(report)):
        # Create a new report by removing the ith level
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            return True
    return False


safe_reports = 0

for report in array_data:
    if is_safe(report) or check_report_with_one_removal(report):
        safe_reports += 1

print(safe_reports)

n = int(input())

intervals = []

for _ in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

# Sort by start time
intervals.sort()

result = []

for start, end in intervals:

    # First interval
    if not result:
        result.append([start, end])

    else:
        last_start, last_end = result[-1]

        # If intervals overlap
        if start <= last_end:
            result[-1][1] = max(last_end, end)

        # If intervals don't overlap
        else:
            result.append([start, end])

# Print answer
for start, end in result:
    print(start, end)
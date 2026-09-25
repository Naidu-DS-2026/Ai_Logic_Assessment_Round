from collections import deque

n = int(input())

arr = list(map(int, input().split()))

k = int(input())

max_deque = deque()
min_deque = deque()

left = 0

best_length = 0
best_start = 1

for right in range(n):

    # Maintain maximum
    while max_deque and arr[max_deque[-1]] <= arr[right]:
        max_deque.pop()

    max_deque.append(right)

    # Maintain minimum
    while min_deque and arr[min_deque[-1]] >= arr[right]:
        min_deque.pop()

    min_deque.append(right)

    # Shrink window if difference > k
    while arr[max_deque[0]] - arr[min_deque[0]] > k:

        if max_deque[0] == left:
            max_deque.popleft()

        if min_deque[0] == left:
            min_deque.popleft()

        left += 1

    # Current window length
    current_length = right - left + 1

    # Update longest window
    if current_length > best_length:
        best_length = current_length
        best_start = left + 1

print(best_length, best_start)
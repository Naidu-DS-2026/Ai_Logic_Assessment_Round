class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(arr):
    head = None
    tail = None

    for value in arr:
        new_node = Node(value)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


def add_two_numbers(l1, l2):
    dummy = Node(0)
    current = dummy

    carry = 0

    while l1 is not None or l2 is not None or carry != 0:

        # Get digit from first list
        if l1 is not None:
            digit1 = l1.data
        else:
            digit1 = 0

        # Get digit from second list
        if l2 is not None:
            digit2 = l2.data
        else:
            digit2 = 0

        # Add digits and carry
        total = digit1 + digit2 + carry

        # Current digit
        digit = total % 10

        # New carry
        carry = total // 10

        # Add digit to result
        current.next = Node(digit)
        current = current.next

        # Move forward
        if l1 is not None:
            l1 = l1.next

        if l2 is not None:
            l2 = l2.next

    return dummy.next


# Input
n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))


# Create linked lists
l1 = create_linked_list(arr1)
l2 = create_linked_list(arr2)


# Add the numbers
result = add_two_numbers(l1, l2)


# Print result
output = []

while result is not None:
    output.append(str(result.data))
    result = result.next

print(" ".join(output))
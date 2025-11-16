def print_list(head, limit=30):
    curr = head
    steps = 0
    while curr and steps < limit:
        print(curr.val, end=' -> ')
        curr = curr.next
        steps += 1
    if curr:
        print('... (cycle or long list)')
    else:
        print('None')

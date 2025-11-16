from ListNode import ListNode

def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for n in arr:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

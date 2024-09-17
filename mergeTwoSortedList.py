
def mergeTwoSortedList(l1, l2):
    dummy = ListNode()
    result = dummy

    while l1 and l2:
        if l1.val < l2.val:
            result.next = l1
            l1 = l1.next
        else:
            result.next = l2
            l2 = l2.next
        result = result.next

    if l1:
        result.next = l1
    if l2:
        result.next = l2

    return dummy.next


def main():
    print(mergeTwoSortedList([1,2,4], [1,3,4]))
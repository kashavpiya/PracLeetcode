def reverseList(arr):
    # needs implementation of listNode to run

        prev, curr = None, arr

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
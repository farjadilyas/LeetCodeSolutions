"""
 21. Merge Two Sorted Lists
 [ Medium ] [ 61.0% ] -- Solved 12/07/2022

 Approach:
 - Use two pointers to keep track of heads of unmerged subsection of the two lists
 - Use one pointer to keep track of the tail of the merged list
 - Compare the two pointers, use add the smaller node to the tail of the merged list

 Time Complexity: O(N)
 Space Complexity: O(1)
"""


def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        head = cur = list1
        list1 = list1.next
    else:
        head = cur = list2
        list2 = list2.next

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next

    rem = list1 if list1 else (list2 if list2 else None)
    if rem:
        cur.next = rem

    return head
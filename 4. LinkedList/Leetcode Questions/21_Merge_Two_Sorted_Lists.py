# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3 = ListNode(-1)      # dummy node
        list3_original = list3

        while list1 and list2:
            if list1.val <= list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next

        if list1 is not None:
            list3.next = list1

        if list2 is not None:
            list3.next = list2

        return list3_original.next


# -------- Helper Functions --------
def build_linked_list(arr):
    dummy = ListNode(-1)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# -------- Driver Code --------
list1 = [1, 2, 4]
list2 = [1, 3, 4]

l1 = build_linked_list(list1)
l2 = build_linked_list(list2)

sol = Solution()
merged_head = sol.mergeTwoLists(l1, l2)

print(linked_list_to_list(merged_head))

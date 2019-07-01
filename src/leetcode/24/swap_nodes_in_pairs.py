
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(head: ListNode) -> ListNode:




        return head


class Test:
    def getNode() -> ListNode:
        firstNode: ListNode = ListNode(1)
        secondNode: ListNode = ListNode(2)
        thirdNode: ListNode = ListNode(3)
        fourthNode: ListNode = ListNode(4)

        firstNode.next = secondNode
        secondNode.next = thirdNode
        thirdNode.next = fourthNode

        return firstNode

    def toList(head: ListNode) -> list:
        l: list = []

        while head is not None:
            l.append(head.val)
            head = head.next

        return l

    def testSwapPairs():
        assert Test.toList(Solution.swapPairs(Test.getNode())) == [2, 1, 4, 3]


if __name__ == "__main__":
    Test.testSwapPairs()

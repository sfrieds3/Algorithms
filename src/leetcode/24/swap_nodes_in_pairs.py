# https://leetcode.com/problems/swap-nodes-in-pairs/

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

        # catch edge cases
        if head is None:
            return head
        if head.next is None:
            return head

        newHead = head.next

        # switch the first two
        tmp = head.next
        head.next = head.next.next
        tmp.next = head
        prevLast = head
        head = head.next

        while head is not None and head.next is not None:
            tmp = head.next
            head.next = head.next.next
            tmp.next = head
            prevLast.next = tmp
            prevLast = head
            head = head.next

        # tmp: ListNode = head.next

        # while nextNode is not None:
        #     tmp = head.next
        #     nextNode = tmp.next
        #     tmp.next = head
        #     head.next = tmp
        #     try:
        #         prevNode.next = tmp
        #     except:
        #         pass
        #     prevNode = head
        #     prevNode.next = None
        #     head = nextNode

        return newHead


class Test:
    def getFourNode() -> ListNode:
        firstNode: ListNode = ListNode(1)
        secondNode: ListNode = ListNode(2)
        thirdNode: ListNode = ListNode(3)
        fourthNode: ListNode = ListNode(4)

        firstNode.next = secondNode
        secondNode.next = thirdNode
        thirdNode.next = fourthNode

        return firstNode

    def getThreeNode() -> ListNode:
        firstNode: ListNode = ListNode(1)
        secondNode: ListNode = ListNode(2)
        thirdNode: ListNode = ListNode(3)

        firstNode.next = secondNode
        secondNode.next = thirdNode

        return firstNode

    def toList(head: ListNode) -> list:
        l: list = []

        while head is not None:
            l.append(head.val)
            head = head.next

        print(l)

        return l

    def testSwapPairs():
        assert Test.toList(Solution.swapPairs(Test.getFourNode())) == [2, 1, 4, 3]
        assert Test.toList(Solution.swapPairs(Test.getThreeNode())) == [2, 1, 3]


if __name__ == "__main__":
    Test.testSwapPairs()

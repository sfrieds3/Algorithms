# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast: ListNode = head
        slow: ListNode = head

        for _ in range(0, n):
            fast = fast.next

        if fast == None:
            head = slow.next
        else:
            while fast.next != None:
                slow = slow.next
                fast = fast.next

            slow.next = slow.next.next

        return head


class Test:
    def createListNode() -> ListNode:
        firstNode: ListNode = ListNode(1)
        secondNode: ListNode = ListNode(2)
        thirdNode: ListNode = ListNode(3)
        fourthNode: ListNode = ListNode(4)
        fifthNode: ListNode = ListNode(5)

        firstNode.next = secondNode
        secondNode.next = thirdNode
        thirdNode.next = fourthNode
        fourthNode.next = fifthNode

        return firstNode

    def createSingleListNode() -> ListNode:
        firstNode: ListNode = ListNode(1)

        return firstNode

    def createTwoListNode() -> ListNode:
        firstNode: ListNode = ListNode(1)
        secondNode: ListNode = ListNode(2)

        firstNode.next = secondNode

        return firstNode

    def toList(head: ListNode) -> ListNode:
        res: list = []

        while head is not None:
            res.append(head.val)
            head = head.next

        print(res)

        return res

    def testRemoveNthFromEnd():
        solution: Solution = Solution()
        assert(Test.toList(solution.removeNthFromEnd(
            Test.createListNode(), 2)) == [1, 2, 3, 5])
        assert(Test.toList(solution.removeNthFromEnd(
            Test.createSingleListNode(), 1)) == [])
        assert(Test.toList(solution.removeNthFromEnd(
            Test.createTwoListNode(), 2)) == [2])


if __name__ == "__main__":
    Test.testRemoveNthFromEnd()

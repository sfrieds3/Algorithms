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
        tmpIndex: int = 0

        storedHead = head

        while head != None:
            tmpIndex = tmpIndex + 1
            head = head.next

        tmp: ListNode = storedHead

        tmpIndex = tmpIndex - n

        currIndex: int = 0

        while currIndex < tmpIndex - 1:
            currIndex = currIndex + 1
            tmp = tmp.next

        if tmpIndex == 0:
            storedHead = storedHead.next
        else:
            tmp.next = tmp.next.next

        return storedHead

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


    def toList(head: ListNode) -> ListNode:
        res: list = []

        while head is not None:
            res.append(head.val)
            head = head.next

        print(res)

        return res


    def testRemoveNthFromEnd():
        solution: Solution = Solution()
        assert(Test.toList(solution.removeNthFromEnd(Test.createListNode(), 2)) == [1, 2, 3, 5])


if __name__ == "__main__":
    Test.testRemoveNthFromEnd()
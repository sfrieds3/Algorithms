package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

	if l1 == nil && l2 == nil {
		return nil
	}

	if l1 == nil {
		l1 = &ListNode{Val: 0}
	}

	if l2 == nil {
		l2 = &ListNode{Val: 0}
	}

	sum := l1.Val + l2.Val

	if sum >= 10 {
		if l1.Next == nil {
			new := ListNode{Val: 1}
			l1.Next = &new
		} else {
			l1.Next.Val = l1.Next.Val + 1
			fmt.Println("l1.Next.Val= ", l1.Next.Val)
		}
	}

	res := ListNode{Val: sum % 10}

	fmt.Println("res.Val = ", res.Val)

	fmt.Println("l1.Val = ", l1.Val, ", l2.Val = ", l2.Val)
	res.Next = addTwoNumbers(l1.Next, l2.Next)

	return &res
}

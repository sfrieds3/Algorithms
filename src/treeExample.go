package main

import "fmt"

type tree struct {
	val   int
	left  *tree
	right *tree
}

/*
      4
    2   6
   1 3 5 7
*/
//fmt.Println("should return: 4, 2, 1, 3, 6, 5, 7")

func main() {
	t := new(tree)
	t1 := new(tree)
	t2 := new(tree)
	t3 := new(tree)
	t4 := new(tree)
	t5 := new(tree)
	t6 := new(tree)

	t.val = 4
	t1.val = 2
	t2.val = 6
	t3.val = 1
	t4.val = 3
	t5.val = 5
	t6.val = 7

	t.left = t1
	t.right = t2
	t1.left = t3
	t1.right = t4
	t2.left = t5
	t2.right = t6

	fmt.Println("BFS:")
	fmt.Println("should return: 4 2 6 1 3 5 7")
	t.beginBFS()

	fmt.Println("DFS:")
	fmt.Println("should return: 4, 2, 1, 3, 6, 5, 7")
	t.beginDFS()
}

func (t *tree) beginBFS() {
	if t == nil {
		return
	}
	fmt.Println(t.val)
	t.treeSearchBreadth()
}

func (t *tree) treeSearchBreadth() {
	if t == nil {
		return
	}
	if t.left != nil {
		fmt.Println(t.left.val)
	}
	if t.right != nil {
		fmt.Println(t.right.val)
	}
	t.left.treeSearchBreadth()
	t.right.treeSearchBreadth()
}

func (t *tree) beginDFS() {
	visited := new([]tree)
	if t == nil {
		return
	}
	fmt.Println(t.val)
	t.treeSearchDepth(visited)
}

func (t *tree) treeSearchDepth(visited *[]tree) {
	// TODO(sfreids3) figure out how to get length of visited slice
	l := make([]tree, 10)
	copy(l, *visited)
	fmt.Println(l)
	if t.left != nil {
		t.left.treeSearchDepth(&l)
	} else {
		fmt.Println(t.val)
		return
	}
	if t.right != nil {
		t.right.treeSearchDepth(&l)
	} else {
		fmt.Println(t.val)
	}
}

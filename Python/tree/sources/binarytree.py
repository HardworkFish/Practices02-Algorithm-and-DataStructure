#!/usr/bin/env python
# Python 实现二叉树

#创建根节点
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
# 插入节点
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# 打印二叉树
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data, end = " ")
        if self.right:
            self.right.PrintTree()


#二叉树的前序遍历
# Root->Left-->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

# 二叉树非递归先序遍历
    def NoPreorderTraversal(self, root):
        res = []
        stack = []
        while root or stack:
            while root:
                res.append(root.data)
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                root = t.right
        return res

#二叉树的中序遍历
# Left->Root->Right
    def InorderTraversal(self, root):
        res = []
        if root:
            res = res + self.InorderTraversal(root.left)
            res.append(root.data)
            res = res + self.InorderTraversal(root.right)
        return res

#二叉树非递归中序遍历
    def NoInorderTraversal(self, root):
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                res.append(t.data)
                root = t.right
        return res

#二叉树的后序遍历
# Left->Right->Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = res + self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

# 非递归的后序遍历
    def NoPostorderTraversal(self, root):
        res = []
        stack = []
        while root or stack:
            while root:
                res.append(root.data)
                stack.append(root)
                root = root.right
            if stack:
                top = stack.pop()
                root = top.left
        return res[::-1]
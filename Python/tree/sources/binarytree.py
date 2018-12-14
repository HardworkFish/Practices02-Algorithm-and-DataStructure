#!/usr/bin/env python
# Python 实现二叉树
# 2018-11-19 22:34


# 创建根节点
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # 插入节点
    def insert(self, node):
        if self.data:
            if node.data < self.data:
                if self.left is None:
                    self.left = node
                else:
                    self.left.insert(node)
            elif node.data > self.data:
                if self.right is None:
                    self.right = node
                else:
                    self.right.insert(node)
        else:
            self.data = node.data

    # 打印二叉树
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right.print_tree()

    # 二叉树的前序遍历
    # Root->Left-->Right
    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

    # 二叉树非递归先序遍历
    @staticmethod
    def no_preorder_traversal(root):
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

    # 二叉树的中序遍历
    # Left->Root->Right
    def inorder_traversal(self, root):
        res = []
        if root:
            res = res + self.inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.inorder_traversal(root.right)
        return res

    # 二叉树非递归中序遍历
    @staticmethod
    def no_inorder_traversal(root):
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

    # 二叉树的后序遍历
    # Left->Right->Root
    def postorder_traversal(self, root):
        res = []
        if root:
            res = res + self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.data)
        return res

    # 非递归的后序遍历
    @staticmethod
    def no_postorder_traversal(root):
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

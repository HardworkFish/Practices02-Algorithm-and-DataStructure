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

#二叉树的中序遍历
# Left->Root->Right
    def InorderTraversal(self, root):
        res = []
        if root:
            res = self.InorderTraversal(root.left)
            res.append(root.data)
            res = res + self.InorderTraversal(root.right)
        return res

#二叉树的后序遍历
# Left->Right->Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(self.data)
        return res

# Day 11 - 41: Advanced Binary Tree Practice
from collections import deque

class Node:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None

root = Node(10)
root.left, root.right = Node(5), Node(15)
root.left.left, root.left.right = Node(3), Node(7)
root.right.left, root.right.right = Node(12), Node(20)

# 1. Preorder
def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left); preorder(node.right)
print("1. Preorder:", end=" "); preorder(root); print()

# 2. Inorder
def inorder(node):
    if node:
        inorder(node.left); print(node.value, end=" "); inorder(node.right)
print("2. Inorder:", end=" "); inorder(root); print()

# 3. Postorder
def postorder(node):
    if node:
        postorder(node.left); postorder(node.right); print(node.value, end=" ")
print("3. Postorder:", end=" "); postorder(root); print()

# 4. Level order
def level_order(node):
    result, q = [], deque([node])
    while q:
        n = q.popleft(); result.append(n.value)
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)
    return result
print("4. Level order:", level_order(root))

# 5. Height
def height(node):
    return 0 if not node else 1 + max(height(node.left), height(node.right))
print("5. Height:", height(root))

# 6. Count nodes
def count(node):
    return 0 if not node else 1 + count(node.left) + count(node.right)
print("6. Node count:", count(root))

# 7. Count leaves
def leaves(node):
    if not node: return 0
    if not node.left and not node.right: return 1
    return leaves(node.left) + leaves(node.right)
print("7. Leaf count:", leaves(root))

# 8. Maximum value
def maximum(node):
    if not node: return float("-inf")
    return max(node.value, maximum(node.left), maximum(node.right))
print("8. Maximum:", maximum(root))

# 9. Search
def search(node, target):
    return bool(node and (node.value == target or search(node.left, target) or search(node.right, target)))
print("9. Search 12:", search(root, 12))

# 10. Mirror tree
def mirror(node):
    if node:
        node.left, node.right = node.right, node.left
        mirror(node.left); mirror(node.right)
mirror(root)
print("10. Mirrored:", level_order(root))

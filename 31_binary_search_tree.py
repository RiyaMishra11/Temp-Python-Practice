# Day 8 - 31: Binary Search Tree
class Node:
    def __init__(self, value):
        self.value=value; self.left=None; self.right=None

def insert(root, value):  # 1
    if root is None: return Node(value)
    if value < root.value: root.left=insert(root.left,value)
    elif value > root.value: root.right=insert(root.right,value)
    return root

def search(root, target):  # 2
    if root is None: return False
    if root.value == target: return True
    return search(root.left,target) if target < root.value else search(root.right,target)

def inorder(root, result=None):  # 3
    result=[] if result is None else result
    if root:
        inorder(root.left,result); result.append(root.value); inorder(root.right,result)
    return result

def preorder(root, result=None):  # 4
    result=[] if result is None else result
    if root:
        result.append(root.value); preorder(root.left,result); preorder(root.right,result)
    return result

def postorder(root, result=None):  # 5
    result=[] if result is None else result
    if root:
        postorder(root.left,result); postorder(root.right,result); result.append(root.value)
    return result

def minimum(root):  # 6
    if root is None: return None
    while root.left: root=root.left
    return root.value

def maximum(root):  # 7
    if root is None: return None
    while root.right: root=root.right
    return root.value

def height(root):  # 8
    return 0 if root is None else 1+max(height(root.left),height(root.right))

def count_nodes(root):  # 9
    return 0 if root is None else 1+count_nodes(root.left)+count_nodes(root.right)

def leaf_count(root):  # 10
    if root is None: return 0
    if root.left is None and root.right is None: return 1
    return leaf_count(root.left)+leaf_count(root.right)

if __name__ == "__main__":
    root=None
    for x in [50,30,70,20,40,60,80]: root=insert(root,x)
    print(search(root,60))
    print(inorder(root), preorder(root), postorder(root))
    print(minimum(root), maximum(root), height(root), count_nodes(root), leaf_count(root))

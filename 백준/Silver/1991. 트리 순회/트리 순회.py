from sys import stdin

def preorder(t, node):
    print(node, end='')
    if t[node][0] != '.':
        preorder(t, t[node][0])
    if t[node][1] != '.':
        preorder(t, t[node][1])

def inorder(t, node):
    if t[node][0] != '.':
        inorder(t, t[node][0])
    print(node, end='')
    if t[node][1] != '.':
        inorder(t, t[node][1])

def postorder(t, node):
    if t[node][0] != '.':
        postorder(t, t[node][0])
    if t[node][1] != '.':
        postorder(t, t[node][1])
    print(node, end='')

n = int(stdin.readline())
tree = {}
for _ in range(n):
    root, left, right = map(str, stdin.readline().split())
    tree[root] = [left, right]
preorder(tree, 'A')
print('')
inorder(tree, 'A')
print('')
postorder(tree, 'A')
print('')
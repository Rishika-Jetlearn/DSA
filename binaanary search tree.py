import treeDS

def insert(start,value):
    if start is None:
        print("Create node")
        return treeDS.tree_node(value)
    elif start.key>value:
        print("Left side")
        start.left_ch=insert(start.left_ch,value)
    else:
        print("Right side")
        start.right_ch=insert(start.right_ch,value)
    return start

def search(root,item):
    if item==root.key:
        return True
    
    elif item> root.key and root.right_ch is not None:
        return search(root.right_ch,item)
    
    elif item<root.key and root.left_ch is not None:
        return search(root.left_ch,item)
    else:
        return False

def inorder_succesor(node):
    successor=node.right_ch
    while successor.left_ch is not None:
        successor=successor.left_ch
    return successor

def delete(root,item):
    if root is None:
        return root
    elif item>root.key:
        root.right_ch=delete(root.right_ch,item)
    elif item<root.key:
        root.left_ch=delete(root.left_ch,item)
    else:
        if root.left_ch is None:
            return root.right_ch
        if root.right_ch is None:
            return root.left_ch
        succ=inorder_succesor(root)
        root.key=succ.key
        root.right_ch=delete(root.right_ch,succ.key)
    return root

root=None
while True:
    user=input("Enter the value for the node or press S to stop")
    if user=="S":
        break
    
    root=insert(root,int(user))

treeDS.inorder(root)
what_item=int(input("Item: "))
print(search(root,what_item))

dele=int(input("Delete: "))
delete(root,dele)
treeDS.inorder(root)
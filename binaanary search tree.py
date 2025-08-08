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

root=None
while True:
    user=input("Enter the value for the node or press S to stop")
    if user=="S":
        break
    
    root=insert(root,int(user))

treeDS.inorder(root)
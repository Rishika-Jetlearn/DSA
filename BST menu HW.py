import treeDS
user=""
while not user=="S":
    user=input("What would you like to do?    Insert node: type insert     Search node: type search     Delete node: type delete")
    #insert
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

    #search
    def search(root,item):
        
            if item==root.key:
                return True
            
            elif item> root.key and root.right_ch is not None:
                return search(root.right_ch,item)
            
            elif item<root.key and root.left_ch is not None:
                return search(root.left_ch,item)
            else:
                return False


    #delete 
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

    if user=="insert":
        start=int(input("please enter the starting value "))
        value=int(input("please enter the value of node "))
        print(insert(start,value))
    elif user=="search":
        root=int(input("please enter the starting value "))
        item=int(input("please enter the item you want to search "))
        print(search(root,item))
    elif user=="delete":
        root=int(input("please enter the starting value "))
        item=int(input("please enter the item you want to search "))
        print(delete(root,item))
    else:
        print("Error :/")
        
from tkinter import*
import treeDS
import copy
window=Tk()
window.geometry("430x500")
window.title("BST")
window.config(background="#C2EBF5")
root=None

#functions
def create_node():
    value=Value_of_node.get()
    global root
    root=treeDS.tree_node(value)
    Value_of_node.delete(0,END)



def insert_node(start,value):
    if start is None:
        print(root.key)
        return treeDS.tree_node(value)
    elif start.key>value:
        print("left",root.key)
        start.left_ch=insert_node(start.left_ch,value)
        
    else:
        print("right",root.key)
        start.right_ch=insert_node(start.right_ch,value)

    Value_of_node.delete(0,END)
    return start    
    

def search_node(start):
    item=int(Value_of_node.get())

    if item==start.key:
        result=True
        tree.config(text="Item is root")
    
    elif item> start.key and start.right_ch is not None:
        result=search_node(start.right_ch)
        tree.config(text=f"{result}")

    elif item<start.key and start.left_ch is not None:
        result=search_node(start.left_ch)
        tree.config(text=f"{result}")
    else:
        result=False
        tree.config(text=f"{result}")

#trversals
def inorder_tvrs(start):
    tree.config(text="")
    print(start.key)
    if start.left_ch is not None:
        inorder_tvrs(start.left_ch)

    result=tree.cget("text") + "," + str(start.key)
    print(result)
    tree.config(text=f"{result}")

    if start.right_ch is not None:
        inorder_tvrs(start.right_ch)

def preorder_tvrs(start):
    tree.config(text="")
    result=tree.cget("text") + "," + str(start.key)
    print(result)
    tree.config(text=f"{result}")

    print(start.key)
    if start.left_ch is not None:
        preorder_tvrs(start.left_ch)

    if start.right_ch is not None:
        preorder_tvrs(start.right_ch)


def postorder_tvrs(start):
    tree.config(text="")
    print(start.key)
    if start.left_ch is not None:
        postorder_tvrs(start.left_ch)

    if start.right_ch is not None:
        postorder_tvrs(start.right_ch)

    result=tree.cget("text") + "," + str(start.key)
    print(result)
    tree.config(text=f"{result}")


#user input
Value_of_node=Entry(window)
Value_of_node.grid(row=1,column=1)

start_lable=Label(window,text="Start: ")
start_lable.grid(row=1,column=0)

#LABELS
lab=Label(window,text="Node value: ",font=("comicsans",16,"bold"))
lab.grid(row=1,column=0)

tree=Label(window,)
tree.grid(row=5,column=0)

#Buttons
create=Button(window,text="Create node",bg="lightgreen",fg="black",command=create_node)
create.grid(row=4,column=2,padx=50,pady=30)

insert=Button(window,text="insert node",bg="lightgreen",fg="black",command=lambda:insert_node(root,Value_of_node.get()))
insert.grid(row=3,column=2,padx=50,pady=30)

search=Button(window,text="search node",bg="lightgreen",fg="black",command=lambda: search_node(root))
search.grid(row=2,column=2,padx=50,pady=30)

exit=Button(window,text="Exit",command=exit,bg="lightgreen",fg="black")
exit.grid(row=2,column=1,padx=50,pady=30)

inorder=Button(window,text="Inorder",bg="lightgreen",fg="black",command=lambda: inorder_tvrs(root))
inorder.grid(row=2,column=0,padx=50,pady=50)

preorder=Button(window,text="Preorder",bg="lightgreen",fg="black",command=lambda: preorder_tvrs(root))
preorder.grid(row=3,column=0,padx=50,pady=30)

postorder=Button(window,text="Postorder",bg="lightgreen",fg="black",command=lambda: postorder_tvrs(root))
postorder.grid(row=4,column=0,padx=50,pady=30)


window.mainloop()
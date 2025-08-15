from tkinter import*
import treeDS
window=Tk()
window.geometry("430x500")
window.title("BST")
window.config(background="#C2EBF5")


def insert_node():
    value=Value_of_node.get()
    start=root.get()
    if start is None:
        print("Create node")
        return treeDS.tree_node(value)
    elif start.key>value:
        print("Left side")
        start.left_ch=insert_node(start.left_ch,value)
    else:
        print("Right side")
        start.right_ch=insert_node(start.right_ch,value)
    return start
    
#user input
Value_of_node=Entry(window)
Value_of_node.grid(row=1,column=1)

start_lable=Label(window,text="Start: ")
start_lable.grid(row=1,column=0)

root=Entry(window)
root.grid(row=2,column=0)

#LABELS
lab=Label(window,text="Node value: ",font=("comicsans",16,"bold"))
lab.grid(row=1,column=0)

tree=Label(window)
tree.grid(row=5,column=0)

#Buttons
create=Button(window,text="Create node",bg="lightgreen",fg="black")
create.grid(row=4,column=2,padx=50,pady=30)

insert=Button(window,text="insert node",bg="lightgreen",fg="black",command=insert_node())
insert.grid(row=3,column=2,padx=50,pady=30)

search=Button(window,text="search node",bg="lightgreen",fg="black")
search.grid(row=2,column=2,padx=50,pady=30)

exit=Button(window,text="Exit",command=exit,bg="lightgreen",fg="black")
exit.grid(row=2,column=1,padx=50,pady=30)

inorder=Button(window,text="Inorder",bg="lightgreen",fg="black")
inorder.grid(row=2,column=0,padx=50,pady=50)

preorder=Button(window,text="Preorder",bg="lightgreen",fg="black")
preorder.grid(row=3,column=0,padx=50,pady=30)

postorder=Button(window,text="Postorder",bg="lightgreen",fg="black")
postorder.grid(row=4,column=0,padx=50,pady=30)


window.mainloop()
list=[3,90,1,23,45,9,15,4]

for i in range(len(list)):
    print(f"pass {i+1}")
    swapped=False
    for b in range(len(list)-1):
        if list[b]>list[b+1]:
        #swapping logic that would work in any language(making a tempory variable)
          temp=list[b]
          list[b]=list[b+1]
          list[b+1]=temp
        # the line below is swapping but only works in python
          "list[b],list[b+1]=list[b+1],list[b]"
          swapped=True
           
        print(list)

    if swapped==False:
        break


print("DEACRASING ORDER ---->")
#DECREASING
list=[3,90,1,23,45,9,15,4]

for i in range(len(list)):
    print(f"pass {i+1}")
    swapped=False
    for b in range(len(list)-1):
        if list[b]<list[b+1]:
            list[b],list[b+1]=list[b+1],list[b]
            swapped=True
           
        print(list)

    if swapped==False:
        break
          


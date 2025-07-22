list=[3,6,2,1,6,99,12]
for i in range(len(list)):
    key=list[i]
    j=i-1
    while j>=0 and key<list[j]:
        list[j+1]=list[j]
        j=j-1
    list[j+1]=key
    print(list)
    print()


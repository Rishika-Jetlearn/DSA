def merge(list,low,mid,high):
    i=low
    j=mid+1
    store=[]
    #as long as I still have items in both sides
    while i<=mid and j<=high:
        if list[i]<list[j]:
            store.append(list[i])
            i=i+1
        else:
            store.append(list[j])
            j=j+1
    #when there is still items left on the left side,just pick them
    while i<=mid:
        store.append(list[i])
        i=i+1
    #when there is still items left on the right side,just pick them
    while j<=high:
        store.append(list[j])
        j=j+1
    k=0
    for i in range(low,high+1):
        list[i]=store[k]
        k=k+1
l=[1,5,2,34,9,45,67,13,12,11,8,3]
merge(l,0,1,3)
print(l)
a=[1,2,5,34,12,15,18,20,3,6,1,2]
merge(a,0,3,7)
print(a)
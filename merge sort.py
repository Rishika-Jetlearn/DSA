def merge(list,low,mid,high):
    i=low
    j=mid+1
    store=[]
    #as long as I still have items in both sides
    while i<=mid and j<=high:
        #take the smaller one and add it to store
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
    #going back to the original list
    k=0
    for i in range(low,high+1):
        list[i]=store[k]
        k=k+1
def merge_sort(list,low,high):
    if low<high:
        mid=(low+high)//2
        merge_sort(list,low,mid)
        merge_sort(list,mid+1,high)
        merge(list,low,mid,high)

l=[1,5,2,34,9,45,67,13,12,11,8,3]
merge_sort(l,0,len(l)-1)
print(l)

list=[1,3,6,7,9,12,67]
user=int(input("What number do you want to find?"))
#(strat+end)//2
found=False
start=0
end= len(list)-1

while start<=end:
    middle=(start+end)//2
    if list[middle]==user:
        found=True
        print(f"Founded at {middle} position")
        break
    elif list[middle]>user:
        end=middle-1
    else:
        start=middle+1

if found==False:
    print("Not Found")


#linear search
list=[2,4,6,11,24,87,53,23,12,89]
user=int(input("enter a number"))
for i in list:
    if user==i:
        print("Found")
    else:
        print("Not found")
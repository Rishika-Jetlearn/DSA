list=[2,4,6,11,24,87,53,23,12,89]
user=int(input("enter a number"))
found=False
for i in range(0,len(list)):
    if user==list[i]:
        print(f"Found at  index {i}") 
        found=True
        break
        
if found==False:
    print("not found")

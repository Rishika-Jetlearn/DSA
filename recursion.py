"""user=int(input("number:"))
total=0
for i in range(1,user+1):
    total=i+total
    print(total)"""

#recurion
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
print(sum(6))
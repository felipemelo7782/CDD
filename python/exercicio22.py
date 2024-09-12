for x in range(1,11):
    print(f" ({x}) ",end="")
for x in range(9,0,-1):
    print(f" ({x}) ",end="")




print("\n------")
for x in range(10,-10,-1):
    if x <=-1:
        x=x*-1
        print(f" ({x}) ", end="")
    else:
        print(f" ({x}) ",end="")
f0=0
f1=1
i=2
n=int(input("Enter the number of terms:"))
print(f0)
print(f1)
while i<n:
    f2=f0+f1
    f0=f1
    f1=f2
    i=i+1
    print(f2)

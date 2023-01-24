def sum(a,b):
    return (a+b)

def avg(a,b):
    return (a+b)/2

def arm(n):
    n=int(input("enter a no."))
sum=0
order=len(str(n))
copy_n=n
while(n>0):
    digit=n%10
    sum+=digit**order
    n=n//10
if(sum==copy_n):
    print(f"{copy_n} is an armstrong no.")
else:
    print(f"{copy_n} is not an armstrong no.")        



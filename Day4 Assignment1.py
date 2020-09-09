# Armstrong no.
lower=1042000
upper=702648265
for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    i=num
    while i>0:
        digit=i%10
        sum+=digit**order
        i//=10

    if num==sum:
            print("The first Armstrong no.is:",num)
            break

















 



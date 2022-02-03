x = int(input('Enter the number : '))
sum=0
for i in range(1,(x//2)+1,1):
    if(x%i == 0):
         sum=sum+i
if(sum == x):
    print('\n Perfect number.')
else :
    print("\n Not a perfect number.")


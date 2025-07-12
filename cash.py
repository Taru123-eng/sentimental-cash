from cs50 import *
while True:
    n=get_float('Change: ')
    if n>0:
        break
    else:
     print('Invalid Input')



cents=round(n*100)

def remaining(n):
  money=[25,10,5,1]
  sum=0
  if n==0:
    return 0
  if n in money:
    sum=1
  for i in range(len(money)):
    if n>money[i]:
      k=money[i]
      break
  else:
      k=1

  remain=n%k
  if remain in money:
    sum+=((n//k)+1)
    return sum
  else:
     return (remaining(remain)+(n//k))
print(remaining(cents))





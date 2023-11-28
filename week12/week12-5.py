a=150000000
b=200000000
c= a%b
print(a,b,c)
while c!=0:
  a=b
  b=c
  c=a%b
  print(a,b,c)
print(b)
ntimes = int(input("How many values to be printed:\n"))
x=0
y=1
c=0

if(ntimes<=0):                              
  print("enter the positive values!\n")

elif(ntimes==1):
  print("The fibonacci series is:\n",ntimes)
  print(x)

else:
  print("Fibonacci Series\n")
  while(c<ntimes):
    print(x)
    z=x+y
    x=y
    y=z
    c+=1

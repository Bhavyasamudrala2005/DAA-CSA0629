def fibnocci(n):
     if n<0 or n==0:
          print("invalid input")
     elif n==1 or n==2:
          return 1
     else:
          return (fabonacci(n-1)+fibonacci(n-2))
n=int(input())
print('fabonacci')

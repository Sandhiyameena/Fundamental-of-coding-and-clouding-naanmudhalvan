# factorial using Recursion (function call itself)
def factorial(n):
 if n == 0:
  return 1
 else:
   return (n*factorial(n-1))
num = 5
print("number:",num)
print("factorial:",factorial (num))
# factroial (7)= 7*6*5*4*3*2*1=5040
# factroial (6)= 6*5*4*3*2*1
# factroial (5)= 5*4*3*2*1
# factroial (4)= 4*3*2*1
# factroial (0)= 1

# factroial (n)= n*factorial(n-1)

def factorial(n):
  if(n == 0 or n==1):
        return 1
  else:
        return n * factorial(n-1)
    
    # test the function

print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(9))
print(factorial(10))

# quick quiz
# write a fionnaci series in python?
from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*5


print(fx(20))
print ("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6 ")

# same as it is upper wala

print(fx(20))
print ("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6 ")
 

a=input("enter the number :")
print(f"multiplacation table of {a} is :")
for i in range(1,11):
 print(f"{int(a)} * {i} = {int(a)*i}")



a=input("enter the number :")
print(f"multiplacation table of {a} is :")
try:
 for i in range(1,11):
  print(f"{int(a)} * {i} = {int(a)*i}")
except:
 print("invalid input")

print("some imp lines of code")
print("end of the program")

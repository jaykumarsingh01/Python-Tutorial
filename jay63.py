import random
def check (cop,user):
  if cop==user:
    return 0
  if(cop==0 and user==1):
    return -1
  if(cop==1 and user==2):
    return -1
  if(cop==2 and user==0):
    return -1

  return 1

cop=random.randint(0,2)
user =int(input("0 for snake ,1 for water and 2 for gun\n"))

score=check(cop,user)
print("You: ",user)
print("computer: ",cop)

if(score==0):
  print("its a draw")

elif(score==-1):
  print("you lose")

else:
  print("you won")
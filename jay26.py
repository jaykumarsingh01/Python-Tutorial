import time

timestamp=time.strftime('%H:%M:%S')
hour= (time.strftime('%H'))

print(timestamp)

timestamp=time.strftime('%H')
print(timestamp)

timestamp=time.strftime('%M')
print(timestamp)

timestamp=time.strftime('%S')
print(timestamp)

hour=int(input("enter your hour:"))
print(hour)

if(hour>=0 and hour<12):
    print("good morning sir: ")

    
elif(hour>=12 and hour<17):
    print("good afteenoon sir: ")

elif(hour>=17 and hour<0):
    print("good night sir: ")
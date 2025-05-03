with open('demo.txt','r') as f:
    f.seek(10)
    data= f.read(5)
    
    print(data)
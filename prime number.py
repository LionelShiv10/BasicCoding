inputcsv = input("")
result = 0
myList = inputcsv.split(',')
if len(myList)<=1000:
    for i in myList:
        if  -1000 <= int(i) <= 1000: 
            result+=int(i)
        else:
            result+=0

print(result)
        
    

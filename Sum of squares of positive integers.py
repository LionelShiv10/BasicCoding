n=int(input(""))


counter=1
result = 0
if 1 <= n <= 1000: 
    while counter <= n:
        result += counter**2
        counter+=1
        

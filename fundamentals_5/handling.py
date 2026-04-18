try:
    x=int(input("enter x:"))
    ans=10/x
    
except ZeroDivisionError: 
    print("dividsion by 0 not allowed ")
    
except ValueError:
    print("invalid input")
    
else:
    print(f"ans ={ans}")
    
finally:
    print("program ended")
with open("PrimeClasses\\fundamentals_5\\sample.txt","r") as f :
    data=True # we created this so that pehli baar mein it works
    line=1
    while(data):
        data=f.readline()
        if("python" in data):
            print(f"word found at line {line} ")
            break 
        print(data)
        line+=1
    
    
    
    
    
    
    